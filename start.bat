del *.pdf
del *.csv
del *.txt
python datenholen.py
pdftotext -raw -eol unix -enc Latin1 Rufzeichenliste_AFU.pdf afu.txt
python convert.py
