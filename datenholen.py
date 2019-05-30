#!/usr/bin/env python
# -*- coding: Windows-1252 -*-
import wget, os


url =('https://ham-digital.org/user_by_id.php')
try:
    os.remove("user_by_id.csv")
except:
    print("Datei bereits geloescht. OK. ", url)
filename = wget.download(url)
print()
url =('https://www.bundesnetzagentur.de/SharedDocs/Downloads/DE/Sachgebiete/Telekommunikation/Unternehmen_Institutionen/Frequenzen/Amateurfunk/Rufzeichenliste/Rufzeichenliste_AFU.pdf?__blob=publicationFile&v=52')
try:
    os.remove("Rufzeichenliste_AFU.pdf")
except:
    print("Datei bereits geloescht. OK. ", url)
filename = wget.download(url)
