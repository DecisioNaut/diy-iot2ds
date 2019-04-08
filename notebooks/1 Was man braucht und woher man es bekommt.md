# Was man braucht und woher man es bekommt!

Bevor man loslegen kann, gibt's schon ein paar Werkzeuge, die gebraucht werden. Hier wird genau aufgelistet, was benötigt wird und woher man es z.B. bekommen kann.

## Grundvoraussetzungen

Um mit dem Raspberry Pi und der Google Cloud kommunizieren zu können, brauchen wir zunächst einfach nur einen Computer und einen Internetzugang (WLAN-Router?). Wir gehen mal davon aus, dass das vorhanden ist, wenn dieses hier gelesen werden kann ;-)

## Eine kleine Einkaufsliste

Die verwendete **Hardware** kostet insgesamt ca. 85 EUR:

- **Raspberry Pi** 3 Model B+ für ca. 35 EUR (erhältlich z.B. bei [Amazon](https://www.amazon.de/Raspberry-1373331-Pi-Modell-Mainboard/dp/B07BDR5PDW/ref=sr_1_5?s=computers&ie=UTF8&qid=1551864649&sr=1-5)).
- **Zubehör-Bundle für den Raspberry** für ca. 24 EUR inkl. Gehäuse mit Lüfter, SD-Karte, SD-Reader, Stromkabel mit Schalter etc. (erhältlich z.B. bei [Amazon](https://www.amazon.de/Raspberry-Smraza-Netzteil-Kühlkörper-Kompatibel/dp/B01L78AE5O/ref=sr_1_68?s=computers&ie=UTF8&qid=1551864540&sr=1-68))
- **Wetter-Sensor** (der im Prinzip auch ein wenig mehr kann) für ca. 19 EUR (erhätlich z.B. bei [Amazon](https://www.amazon.de/WINGONEER-Temperatur-Luftfeuchtigkeit-Sensormodul-Stützstapel/dp/B076SM2YG6/ref=sr_1_fkmr1_3?ie=UTF8&qid=1551865283&sr=8-3-fkmr1))
- **Kabel zum Anstecken des Sensors** für ca. 7 EUR (erhältlich z.B. bei [Amazon](https://www.amazon.de/Female-Female-Male-Female-Male-Male-Steckbrücken-Drahtbrücken-bunt/dp/B01EV70C78/ref=pd_bxgy_img_2/261-5391223-3170926?_encoding=UTF8&pd_rd_i=B01EV70C78&pd_rd_r=18f290c9-5164-11e9-a261-d16e70736dca&pd_rd_w=Xm96L&pd_rd_wg=nuRWs&pf_rd_p=449f5fd6-8f81-46b7-aa57-ca96572671a1&pf_rd_r=3BATMRXANMY73F7W9A30&psc=1&refRID=3BATMRXANMY73F7W9A30))

![Bilder von allem]()

Es wäre prinzipiell auch möglich, den Preis eine ganze Ecke zu drücken. Man könnte eine abgespecktere Version des Raspberry zu verwenden, statt des vorgeschlagenen Zubehör-Bundles ein einfacheres zu nutzen oder bereits vorhandene Teile (z.B. SD-Karten und -Reader) zu verwenden und auch einen einfacheren und billigeren Sensor zu verwenden. Vermutlich käme man spartanisch auch mit etwa 40 EUR aus. Aber das haben wir nicht getestet und schlagen es deshalb auch hier nicht vor.

Die verwendete **Software** gibt's für umme:

- Software bzw. Scripte, die der Raspberry benötigt, um sich selbständig mit dem Netz zu verbinden, die Wetterdaten aus dem Sensor auszulesen und sie in die Cloud zu pushen, sind in diesem Repo abgelegt. Wie das genau funktioniert, darauf gehen wir in den nächsten Kapiteln ein.
- Alle sonstige "Software", die wir nutzen, sind Anwendungen von Google, die in der Cloud laufen und über das Internet erreichbar sind. Welche Anwendungen, das sind und wie wir sie nutzen, wird in den nächsten Kapiteln gezeigt. Alles geht mit einem einfachen **Google-Account**. Einen Google-Account gibt's umsonst (und vielleicht ist schon einer vorhanden). Da das Projekt allerdings nicht für Sicherheitsaspekte optimiert ist, ***empfehlen wir einen separaten Account anzulegen, der später ggf. auch gelöscht werden kann***. Dies zeigen wir im folgenden.

## Einen neuen Google Account erzeugen (und wie er gelöscht werden kann)

Wie zuvor beschrieben, ist das Projekt nicht für Sicherheitsaspekte optimiert. Wir empfehlen daher, einen separaten Google Account mit folgenden Schritten anzulegen, der später auch wieder gelöscht werden kann.

Ein Google Account kann direkt von der [Google-Startseite](https://www.google.com) aus erstellt werden:
</br><img src="./pics/1-02_registration.png" width=600 style="border:1px solid black">
</br>
Von dort wird man durch den weiteren Prozess gut geführt (und ist danach automatisch eingeloggt und kann über den Browser auf sein Konto zugreifen).

Auch das Löschen eines Accounts geht einfach, indem man sich in sich in sein Konto einloggt...
</br><img src="./pics/1-03_deletion-1.png" width=600 style="border:1px solid black">
</br>
... und in den Kontoeinstellungen im Menüpunkt "Daten und Personalisierung" das Untermenü für "Dienst oder Konto löschen" wählt und dort den weiteren Anweisungen folgt:
</br><img src="./pics/1-03_deletion-2.png" width=600 style="border:1px solid black">
</br>
