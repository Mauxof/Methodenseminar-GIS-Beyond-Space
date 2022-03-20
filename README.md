# Methodenseminar-GIS-Beyond-Space

Hinweis: dieser Code wurde im Rahmen eines Seminars an der Friedrich-Alexander-Universität Erlangen-Nürnberg erstellt und basiert teilweise auf externen Quellen. Die Autoren dieses Repository erheben keinen Anspruch auf Urheberschaft, der Code steht zur freien Vefügung. Die erwähnten Pythonskripte liegen immer in einfacher Ausführung am Beispiel des SZ-Korpus vor und können für den taz-Korpus analog angewendet werden (entsprechende Dateinamen müssen getauscht werden).

Ablauf:
1. Durchführen einer Named-Entity Recognition mit Hilfe des Softwarepakets stanza: öffne stanza_pipeline_new.py
2. Geokodierung der erhaltenen csv Datei mit Hilfe des Softwarepakets geopy und dem Gazeteer GeoNames --> Erhalten einer Klassifizierung administrativer Ebenen ('fcode'): fcodes.py
3. Erstellen von Kuchendiagrammen mit Hilfe von Ploty Express: Pie Charty.py
4. Erstellen von Länderkarten mit Hilfe von Folium (die CSV Dateien wurden vorher bereinigt, siehe sz_countries_new.csv und taz_countries.csv): Countriesmap.py
