#!/usr/bin/env python
# -*- coding: Windows-1252 -*-
import pandas as pd, os, re, sys 
#
print("Ver 1.0")
#--------------
# Von PDF nach TXT konvertierte Liste lesbar umwandeln
#
def fix(str):
	str = re.sub("Seite [0-9]{1,3}", "", str)
	str = re.sub("[1-6][\s]*Liste der.*", "", str)
	str = re.sub("ü", "ue", str)
	str = re.sub("ö", "oe", str)
	str = re.sub("ä", "ae", str)
	str = re.sub("Ä", "Ae", str)
	str = re.sub("Ü", "Ue", str)
	str = re.sub("Ö", "Oe", str)
	str = re.sub("ß", "ss", str)
	str = re.sub("\x9f", "n", str)
	str = re.sub("\xa4", "3", str)
	str = re.sub("\xb6", " ", str)
	str = re.sub("\xbc", " ", str)
	str = re.sub("\xc3", "A", str)
	str = re.sub("\"", "", str)
	str = re.sub("\n", "", str)
	str = re.sub("\f", "", str)
	return str
	
def fixCity(str):
	#insert dash
	pos = re.search("[a-z][A-Z]",str)
	if pos == None:
		return str
	else:
		pos = pos.start()
		return str[0:pos+1]+"-"+str[pos+1:]
print ("BNetzA Daten sortieren")
calls = [] #will be the array of calls
call = ""	#for reading lines
incall = False
with open('afu.txt', encoding = 'cp1252') as f:
	for line in f:						
		#match call sign
		if re.match("D[A-R]+[0-9]+[A-Z]+", line): #match call sign
			if call != "":
				calls.append(fix(call))
				call = ""
			call = line
		else:
			if call != "":
				call = call + line	

calls.append(fix(call)) #flush
datei = open("bnetza.csv","w", encoding = 'cp1252')
datei.write("CALLSIGN;NAME;STRASSE;ORT\n")
print("BNetzA Liste in CSV wandeln")
#now process data
for call in calls:
	fields = call.split(";")
	callsign = fields[0].split(",")[0]
	callclass = fields[0].split(",")[1]
	name = fields[0].split(",")[2]
	name = re.sub("^[\s]*", "", name)
	name = re.sub("[\s]*$", "", name)
	callclass = re.sub("^[\s]*", "", callclass)
	if len(fields) == 1:	#no address given
		
		datei.write(callsign + ";" +  name + ";;\n")
		
	else:
		if len(fields) == 3:	#one address given
			street = fields[1]
			street = re.sub("^[\s]*", "", street)
			street = re.sub("[\s]*$", "", street)
			city = fields[2].split(",")[0]	#just in case, there are some errors in the PDF eg DB0ATV
			city = re.sub("^[\s]*", "", city)
			city = re.sub("[\s]*$", "", city)
			zip = city[0:5]
			if city[5] == " ":
				city = city[6:]
			else:
				city = city[5:]  
			city = fixCity(city)
			plzcity = zip + ' '+city
			datei.write(callsign + ";" + name + ";" + street + ";" + plzcity + "\n")
			#print(".", end="")
			
		elif len(fields) == 4:	#two addresses given
			street1 = fields[1]
			street1 = re.sub("^[\s]*", "", street1)
			street1 = re.sub("[\s]*$", "", street1)
			city1 = fields[2].split(",")[0]
			street2 = fields[2].split(",")[1]
			city2 = fields[3]
			street1 = re.sub("^[\s]*", "", street1)
			street1 = re.sub("[\s]*$", "", street1)
			city1 = re.sub("^[\s]*", "", city1)
			city1 = re.sub("[\s]*$", "", city1)
			zip1 = city1[0:5]
			city1 = city1[6:]
			street2 = re.sub("^[\s]*", "", street2)
			street2 = re.sub("[\s]*$", "", street2)
			city2 = re.sub("^[\s]*", "", city2)
			city2 = re.sub("[\s]*$", "", city2)
			zip2 = city2[0:5]
			city2 = city2[6:]
			city1 = fixCity(city1)
			city2 = fixCity(city2)
			plzcity = zip1 + ' '+city1
			datei.write(callsign +';'+ name +';'+ street +';'+ plzcity + "\n")
			#print(".", end="")
datei.close()
print()
print("CSV erzeugt!")
#----------------
# HAM-DMR-Liste 
dmrliste = open("user_by_id.csv", encoding = 'cp1252').readlines()
anzahl_zeilen = len(dmrliste)
print ("DMR-Liste filtern und kuerzen")
datei = open("dmr.csv","w", encoding = 'cp1252')
datei.write("ID;CALLSIGN;CNT\n")
for i in range(anzahl_zeilen-1):
  zeile = list(map(str.strip, dmrliste[i].split(';')))
  if zeile[5] == 'DEU':
    puffer = zeile[1]+';'+zeile[2]+';'+zeile[5]+'\n'
    datei.write(puffer)
datei.close()
#----------------
print("static.users erzeugen")
df2 = pd.read_csv('dmr.csv', sep=';', encoding = 'cp1252')
df1 = pd.read_csv('bnetza.csv', sep=';', encoding = 'cp1252')
erg=df2.merge(df1,on='CALLSIGN')
erg.to_csv("temp.txt", sep=';', encoding = 'cp1252')
fobj_in = open("temp.txt", encoding = 'cp1252')
fobj_out = open("static.users","w", encoding = 'cp1252')
dummy = (fobj_in.readline())
i = 1
for line in fobj_in:
    zeile = list(map(str.strip, line.split(';')))
    puffer = zeile[1]+','+zeile[2]+','+zeile[4]+','+zeile[5]+','+zeile[6]+',,'+zeile[3]+'\n'
    fobj_out.write(puffer)
    i = i + 1
fobj_in.close()
fobj_out.close()
os.remove("temp.txt")
print("static.users erzeugt")