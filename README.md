# MD380static.users
Download der Liste von Funkamateuren von der Bundesnetzagentur im PDF-Format. Umwandeln der Liste in Textformat durch xpdf. Liste in CSV wandeln. (Teile des Codes von DK1UT modifiziert wiederverwendet. Gefunden in der Repo von DL6AKU). Download der DMR-ID Liste von ham-digital. Dort die deutschen OMs filtern. Als nächstes mit der Liste der BNetzA verheiraten. Das Ergebnis ist eine static.users Datei, welche direkt in die VM von Warren Merkel (KD4Z) https://github.com/KD4Z hochgeladen werden kann.

Hinweis! Aufgrund der Gesetze zum Datenschutz dürfen diese extrahierten Daten nur für den persönlichen Bedarf gespeichert werden. Eine Weitergabe an Dritte oder eine direkte Downloadmöglichkeit im Netz ist nicht zulässig. Eine Installation dieser Programme auf öffentlich erreichbaren Servern ist demzufolge ebenfalls nicht gestattet.

Keine Gewähr für dauerhafte Funktion. Es steht und fällt mit den Daten, welche die BNetzA und Hamdigital zur Verfügung stellen.

Benötigt wird:
Python3 (https://www.python.org/)

Pandas (https://pandas.pydata.org/)

wget (für Windows nutze ich diese Version https://pypi.org/project/python3-wget/)
unter Linux lieber direkt curl

xpdf (http://www.xpdfreader.com/download.html) unter Debian / Ubuntu NICHT die offiziellen Paketquellen nehmen, da Absturzgefahr!
Unter Windows die Datei pdftotext.exe direkt in den Ordner kopieren!

Einfach den Installationsanleitungen der Pakete folgen.

Für Windows und Linux habe ich je eine Startdatei erstellt. Dort werden im ersten Schritt die Rohdaten aus dem Web geholt. Über Linux mit curl, über Windows mit datenholen.py. Danach wird die PDF der BNetzA direkt mit pdftotext in die Datei afu.txt umgewandelt. Danach folgt der Aufruf von convert.py. Wenn alles geklappt hat, befindet sich kurze Zeit später die Datei static.users im Verzeichnis.

Von der Nutzung von Python2 rate ich ab, da Pandas für Python 2 nicht mehr weiterentwickelt wurde und die Installation nicht mehr funktioniert.

Die Datei der Bundesnetzagentur wird immer nur Anfang jedes Monats aktualisiert. Die Daten von Hamdigital fortlaufend. Von täglicher Aktualisierung rate ich dennoch ab, da ist der Nutzen eher marginal. Ausserdem werden die Server unnötig belastet. Ich habe es mir zur Regel gemacht, dass ich immer dann ein Update fahre, wenn im Brandmeisternetz mal wieder eine unbekannte deutsche ID erscheint. Zudem nicht alle taufrischen OMs sofort in der BNetzA Liste auftauchen.

Service für Windows-Nutzer, welche kein Python installieren möchten. Hier gibt es ein bereits kompiliertes Paket. https://files.dg1yfx.de/md380static.zip
