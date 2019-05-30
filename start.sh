#!/bin/sh -e

rm ./*.pdf
rm ./*.csv
rm ./*.txt
rm ./*.users
echo "Alte Dateien geloescht"
curl "https://www.bundesnetzagentur.de/SharedDocs/Downloads/DE/Sachgebiete/Telekommunikation/Unternehmen_Institutionen/Frequenzen/Amateurfunk/Rufzeichenliste/Rufzeichenliste_AFU.pdf?__blob=publicationFile&v=52" > Rufzeichenliste_AFU.pdf
curl "https://ham-digital.org/user_by_id.php" > user_by_id.csv
echo "Neue Dateien geholt"
pdftotext -raw -eol unix -enc Latin1 Rufzeichenliste_AFU.pdf afu.txt
echo "PDF in TEXT umgewandelt"
python3 convert.py
echo fertich!

