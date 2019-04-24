![BIRDS LOGO]()

TO DOS:
- Birds Logo einfügen
- Disclaimer prüfen lassen?
- Foto der "Einkäufe"
- Fotos+eigene Skizze für die Verkabelung
- Outlier kalibieren (und Cronjob 120 Sekunden vor Start warten lassen, damit sich die Raspi-Uhr synchronisiert)
- Outlier markieren

# **Do it Yourself!** In der Cloud von Internet-of-Things bis Data Science

## Darum geht's

Begriffe wie "Internet of Things" (IoT), "Cloud" und "Data Science" klingen spannend, erscheinen den meisten aber eher abstrakt und abseits ihrer Kompetenzen.  

In diesem kleinen Projekt wollen wir das alles - insbesondere für Anfänger - mit günstigen Mitteln und Schritt für Schritt erleb- und anfassbar machen. Es geht dabei explizit nicht um Theorie und Hintergründe, sondern der Spaß am Basteln und das gute Gefühl, "Hightech" mal selber zum Laufen gebracht zu haben, stehen absolut im Vordergrund.  

![BILD z.B. End-to-End-Handwerker oder sowas]()

Konkret wollen wir einen 
- Kleinstcomputer ("Raspberry Pi") zum Laufen bringen, mit einem
- Wetter-Sensor verbinden und die generierten Daten automatisiert in die 
- Google-Cloud schieben. Dort können wir die Daten mit
- Data Science-Algorithmen visualisieren und analysieren

Wer also mal eine komplette "End-to-End-Strecke" voller wild klingender Themen abschreiten möchte, folge einfach dieser Anleitung in folgenden Kapiteln:

<ol>
<li><a href="#chapter_1">"Zutaten" und Einkaufsliste</a></li>
<li><a href="#chapter_2">Aufwärmen - den Raspberry zum Laufen bringen</a></li>
<li><a href="#chapter_3">Mit Wetterdaten in die Wolke - IoT spricht mit Cloud</a></li>
<li><a href="#chapter_4">Ein wenig Data Science...</a></li>
</ol>


> ### *Wichtige Hinweise* (TO BE CHECKED BY LAWYER?)
- Dieses Projekt wurde im April und Mai 2019 erstellt und getestet - auf Grund von möglichen Änderungen der Hard- und Software und der jeweiligen Lizenzen kann es sein, dass zukünftig einzelne Schritte nicht mehr funktionieren und/oder rechtlich eingeschränkt oder gar ausgeschlossen werden. Birds on Mars übernimmt keine Gewähr und Verantwortung für die diesbezügliche Aktualität der vorliegenden Projektanleitung
- Dieses Projekt ist - um es einfach zu halten - nicht vor dem Hintergrund von Sicherheitsaspekten optimiert. Wir empfehlen daher, einen separaten Google Account zu nutzen, der nach dem Projekt gelöscht werden kann.
- Wir installieren zwar einen Wettersensor weisen aber darauf hin, dass der Aufbau nicht vor Feuchte und Regen geschützt ist. Um die Gefahr von Stromschlägen zu vermeiden und die Hardware zu schützen, darf der Aufbau und die Durchführung nur und ausschließlich in trockenen Umgebungen erfolgen.
- Dieses Projekt lehnt sich an den Blog-Eintrag von [whatimade.today](http://www.whatimade.today/log-sensor-data-straight-to-google-sheets-from-a-raspberry-pi-zero-all-the-python-code/) an, ist allerdings insbesondere hinsichtlich der Ausführlichkeit der Anleitung und um einen Machine-Learning-Teil erweitert.

<a id='chapter_1'></a>
## 1. "Zutaten" und Einkaufsliste

Bevor man loslegen kann, gibt's ein paar Werkzeuge, die gebraucht werden.  
Hier wird genau aufgelistet, was benötigt wird und woher man es z.B. bekommen kann.

### Grundvoraussetzungen

Um mit dem Raspberry Pi und der Google Cloud kommunizieren zu können, brauchen wir zunächst einfach nur einen
- Computer inkl. einer 
- USB-Tastatur, einer 
- USB-Maus und eines
- Monitors mit HDMI-Ports, einen 
- Internetzugang über WLAN (alternativ: LAN-Zugang mit Kabel) und einen
- Kreuzschlitzschraubenzieher und eine kleine Flachzange (zum Zusammenschrauben)

Wir gehen mal davon aus, dass das vorhanden ist.

### "Einkaufsliste"

Die verwendete **Hardware** kostet insgesamt ca. 85 EUR:

- **Raspberry Pi** 3 Model B+ für ca. 35 EUR (erhältlich z.B. bei [Amazon](https://www.amazon.de/Raspberry-1373331-Pi-Modell-Mainboard/dp/B07BDR5PDW/ref=sr_1_5?s=computers&ie=UTF8&qid=1551864649&sr=1-5)).
- **Zubehör-Bundle für den Raspberry** für ca. 24 EUR inkl. Gehäuse mit Lüfter, SD-Karte, SD-Reader, Stromkabel mit Schalter etc. (erhältlich z.B. bei [Amazon](https://www.amazon.de/Raspberry-Smraza-Netzteil-Kühlkörper-Kompatibel/dp/B01L78AE5O/ref=sr_1_68?s=computers&ie=UTF8&qid=1551864540&sr=1-68))
- **Wetter-Sensor** (der im Prinzip auch ein wenig mehr kann) für ca. 19 EUR (erhätlich z.B. bei [Amazon](https://www.amazon.de/WINGONEER-Temperatur-Luftfeuchtigkeit-Sensormodul-Stützstapel/dp/B076SM2YG6/ref=sr_1_fkmr1_3?ie=UTF8&qid=1551865283&sr=8-3-fkmr1))
- **Kabel zum Anstecken des Sensors** für ca. 7 EUR (erhältlich z.B. bei [Amazon](https://www.amazon.de/Female-Female-Male-Female-Male-Male-Steckbrücken-Drahtbrücken-bunt/dp/B01EV70C78/ref=pd_bxgy_img_2/261-5391223-3170926?_encoding=UTF8&pd_rd_i=B01EV70C78&pd_rd_r=18f290c9-5164-11e9-a261-d16e70736dca&pd_rd_w=Xm96L&pd_rd_wg=nuRWs&pf_rd_p=449f5fd6-8f81-46b7-aa57-ca96572671a1&pf_rd_r=3BATMRXANMY73F7W9A30&psc=1&refRID=3BATMRXANMY73F7W9A30))

![Bilder von allem]()

Es wäre prinzipiell auch möglich, den Preis eine ganze Ecke zu drücken: man könnte eine abgespecktere Version des Raspberry zu verwenden, statt des vorgeschlagenen Zubehör-Bundles ein einfacheres nutzen oder bereits vorhandene Teile (z.B. SD-Karten und -Reader) verwenden und auch einen einfacheren und billigeren Sensor verwenden. Vermutlich käme man spartanischer auch mit etwa 40 EUR aus. Aber das haben wir nicht getestet und schlagen es deshalb auch hier nicht vor.

Die verwendete **Software** gibt's für umme:

- Software bzw. Skripte, die der Raspberry benötigt lassen sich alle aus dem Netz laden. Wie das geht, beschreiben wir in Kapitel 2.
- Alle sonstige "Software", die wir nutzen, sind Anwendungen von Google, die in der Cloud laufen und über das Internet erreichbar sind. Welche Anwendungen das sind und wie wir sie nutzen, wird in den Kapitel 3 und 4 gezeigt. Das alles geht mit einem einfachen **Google-Account**, den es kostenlos gibt. Vielleicht ist schon einer vorhanden; da das Projekt allerdings nicht für Sicherheitsaspekte optimiert ist, ***empfehlen wir einen separaten Account anzulegen, der später ggf. auch gelöscht werden kann***. Dies zeigen wir im Folgenden:

#### Einen neuen Google Account erzeugen (und löschen)

Ein Google Account kann direkt von der [Google-Startseite](https://www.google.com) aus **erstellt** werden:  

<img src="./pics/1-02_registration.png" width=600 style="border:1px solid black"></br>  

Von dort wird man durch den weiteren Prozess gut geführt (und ist danach automatisch eingeloggt und kann über den Browser auf sein Konto zugreifen).

Auch das **Löschen eines Accounts** geht einfach, indem man sich ggf. in sein Konto einloggt...  

<img src="./pics/1-03_deletion-1.png" width=600 style="border:1px solid black"></br>  

... und in den Kontoeinstellungen im Menüpunkt "Daten und Personalisierung" das Untermenü für "Dienst oder Konto löschen" wählt und dort den weiteren Anweisungen folgt:  

<img src="./pics/1-03_deletion-2.png" width=600 style="border:1px solid black"></br>  

<a id='chapter_2'></a>
## 2. Aufwärmen - den Raspberry zum Laufen bringen

Ein Raspberry Pi ist ein Kleinstcomputer, der von der Raspberry Pi Foundation, einer britischen Stiftung, 2012 erstmalig angeboten wurde. Ziel der Stiftung und ihres Produktes ist es, Menschen den Zugang zu Hardware- und Programmierkenntnissen zu erleichtern und das Verständnis der Grundlagen zu fördern. 

Ein Raspberry sieht aus, als hätte man ein Elektronikteil aus einem Radio geschraubt, ist aber ein vollwertiger und erstaunlich vielseitig erweiterbarer Computer. Er erfreut sich bei Bastlern und für Schulungszwecke großer Beliebtheit. Es wurden bereits rd. 20 Millionen Exemplare verkauft.

Ausführliche Informationen, Software, Anleitungen, eine Community etc. finden sich auf [raspberrypi.org](https://www.raspberrypi.org/)

### Schrauberglück

Nicht nur um Kosten zu sparen, ist ein Raspberry auf das Wesentlichste reduziert: nur eine Platine mit Chip und Anschlüssen und Steckverbindungen - kein Display, keine Tastatur. Man kann sich an ihm quasi das Skelett eines Rechners ansehen und über die Steckverbindungen alles Mögliche wie Kameras, Sensoren, Roboterarme usw. usf. anbringen.

Um den Raspberry ein wenig zu schützen (und weil's cooler aussieht) schrauben wir den Raspberry in ein kleines Gehäuse (ein sogenanntes "Rack"). Eine Bauanleitung liegt bei. Wer's ganz genau sehen möchte, kann sich auch folgende kleine Videoanteilung und https://www.youtube.com/watch?v=i7Gw-wb1sfk ansehen:
 
<a href="http://www.youtube.com/watch?feature=player_embedded&v=i7Gw-wb1sfk
" target="_blank"><img src="http://img.youtube.com/vi/i7Gw-wb1sfk/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="600" height="400" border="0" /></a>


### System in den Betrieb bringen

> **Dieser Teil dauert insgesamt rund eine Stunde**, ohne dass allzu viel Spannendes passiert. Man kann aber gut einen Kaffee dabei trinken ;-) **Wer dieses Projekt zusammen mit Freunden/Kollegen durchführen möchte, kann diesen Schritt vorab vorbereiten** (auch ohne vorher das Gehäuse zusammenzubauen, was rasch geht und "Neulingen" vermutlich Spaß macht).

Nach dem Zusammenschrauben kann der Raspberry (noch) nichts. Ihm fehlt das Betriebssystem, mit dem die diversen Komponenten funktionieren und miteinander sprechen können. Da es je nach Anwendungszweck und -anforderungen verschiedene Betriebssysteme gibt, mit denen der Raspberry funktionieren kann, ist noch nichts vorinstalliert. Wir müssen das Betriebssystem unserer Wahl erst auf einer leeren/formatierten SD-Karte installieren (ist im gekauften Bundle ebenso dabei wie ein SD-Kartenleser). Oft - und auch hier - wird Raspbian, das auf Linux basiert, genutzt. Man kann das Betriebssystem von der [raspberrypi.org](https://www.raspberrypi.org/downloads/raspbian/)-Seite (https://www.raspberrypi.org/downloads/raspbian/) auf seinen Rechner herunterladen.  

Wir laden uns die Version **"Raspberry Strech with desktop and recommended software"** als zip-File herunter (knapp 2 GB, dauert also i.d.R. ein paar Minuten) ...  

<img src="./pics/2_download_software.png" width=600 style="border:1px solid black"></br>  

... und ent-zippen das Ganze (hat danach gut 5 GB).  

Das weitere Prozedere ist auch knapp auf der [raspberrypi.org](https://www.raspberrypi.org/documentation/installation/installing-images/README.md)-Seite beschrieben (https://www.raspberrypi.org/documentation/installation/installing-images/README.md ). 

Hier aber eine etwas ausführlichere Darstellung (und auf Deutsch): 

Das Betriebssystem kann nicht einfach auf die SD-Karte kopiert werden; es muss ein "boot-fähiges Image gebrannt" werden. Das geht einigermaßen komfortabel mit dem Programm [**"Etcher"**](https://www.balena.io/etcher/), das es für Windows, MacOS und Linux gibt und das wir unter dieser Adresse https://www.balena.io/etcher/ herunterladen (ca. 100 MB) und dann installieren können. 

Dann folgende Schritte: 
- Leere/formatierte SD-Karte in den Kartenleser stecken, 
- mit dem Rechner verbinden, 
- Etcher starten und 
- "flashen" (was eine knappe halbe Stunde in Anspruch nehmen kann):  

<img src="./pics/2_flash.png" width=600 style="border:1px solid black"></br>  

Damit sich das Betriebssystem vollständig entpackt und initialisiert, müssen wir die 
- SD-Karte in den kleinen Slot an der Seite des Raspberry stecken, den 
- Raspberry mit der USB-Tastatur und -Maus sowie dem HDMI-Bildschirm verbinden und 
- ihn dann ein - aber <u>erst dann!</u> - einschalten (weil der Raspberry sonst z.B. den Bildschirm nicht erkennen kann, da er nicht ohne weiteres Plug-and-Play-fähig ist).  

**Das erste Booten und System-Update** des Raspberry dauert wegen des Entpackens des Systems und dem Download der Updates ca. 20min:
- So sieht nach einer Weile Warten der Startbildschirm aus:  
</br><img src="./pics/2_boot_welcome.png" width=400 style="border:1px solid black">  
- Dann können/sollten die Landeseinstellungen angepasst werden:  
</br><img src="./pics/2_boot_country_settings.png" width=400 style="border:1px solid black">  
- Anschließend sollte aus Sicherheitsgründen das Passwort für den Raspberry angepasst werden (und bitte notieren!):  
</br><img src="./pics/2_boot_password.png" width=400 style="border:1px solid black">  
- Außerdem brauchen wir eine WLAN-Verbindung (ggf. ist natürlich ein Passwort erforderlich):  
</br><img src="./pics/2_boot_wifi.png" width=400 style="border:1px solid black">  
- Dann sollte man die Software zur Sicherheit auf den neuesten Stand bringen (was einige Zeit dauert):  
</br><img src="./pics/2_boot_update.png" width=400 style="border:1px solid black">  
- Zuletzt muss das System nochmals rebooten:  
</br><img src="./pics/2_boot_reboot.png" width=400 style="border:1px solid black">  

**Uffz! Fertig!** ... und bestimmt genug Kaffee für heute getrunken.

<a id='chapter_3'></a>
## Mit Wetterdaten in die Wolke - IoT spricht mit Cloud

Die nachfolgenden Schritte sind etwas tricky. Daher sind sie sehr detailliert beschrieben.
Zunächst bauen wir das
<ol style="list-style-type:lower-latin">
    <li><a href="#chapter_3-1">Setup für die Verbindung mit Google</a> auf, kümmern uns dann um das </li>
    <li><a href="#chapter_3-2">Anschließen des Sensors</a> und führen dann</li>
    <li><a href="#chapter_3-3">Download und Konfiguration der Software für den Raspberry</a> durch.</li>
</ol>  
Wir wählen diese Reihenfolge, damit wir die konfigurierte Software am Ende auch direkt testen können.

<a id='chapter_3-1'></a>
### 3.a Setup für die Verbindung mit Google

Zunächst bleiben wir mal auf dem Raspberry und loggen uns in unseren Account ein (s. 1.; der Browser öffnet sich durch Klicken auf den kleinen Globus oben links in Bildschirm):  
</br><img src="./pics/3_google_login_1.png" width=600 style="border:1px solid black">
</br><img src="./pics/3_google_login_2.png" width=600 style="border:1px solid black">
</br><img src="./pics/3_google_login_3.png" width=600 style="border:1px solid black">  

Nun basteln wir uns die **<u>Google Tabelle</u>, in die wir später die Daten pushen**.  
Wohlgemerkt liegen diese Tabelle und später die Daten in der Google-Cloud. D.h. wir können später von überall und jederzeit darauf zugreifen.  

Erstmal suchen wir nach "Google Tabellen" (ist der kürzeste Weg...) und klicken den ersten Link (http://www.google.de/intl/de/sheets/about/ ):

<img src="./pics/3_google_table_1.png" width=600 style="border:1px solid black"></br>  

Damit wechseln wir in die Cloud-Applikation ... 

<img src="./pics/3_google_table_2.png" width=600 style="border:1px solid black"></br>  

... und übergehen mal die Tour, indem wir das kleine Kreuz anklicken, ...

<img src="./pics/3_google_table_3.png" width=600 style="border:1px solid black"></br>  

... und legen gleich mit einer neuen leeren Tabelle los ("Leer"):

<img src="./pics/3_google_table_4.png" width=600 style="border:1px solid black"></br>  

Wir benennen die Tabelle (oben links) passend mit "diy-iot2ds" ...

<img src="./pics/3_google_table_5.png" width=600 style="border:1px solid black"></br>  

... bennen den Tabellenreiter (unten links) mit "Daten" ...

<img src="./pics/3_google_table_6.png" width=600 style="border:1px solid black"></br>  

... und bennen die Spalten A bis D in der Zeile 1 mit "Zeit", "Temperatur", "Luftdruck" und "Luftfeuchtigkeit":

<img src="./pics/3_google_table_7.png" width=600 style="border:1px solid black"></br>  


Zuletzt merken wir uns für später die **ID-Nummer der Tabelle**.   
Der Zugriff auf die Tabelle erfolgt nämlich im engeren Sinne nicht über den vermeintlichen Dateinamen, sondern über eine längliche innerhalb der Google-Cloud erzeugte ID, die sich aber einfach aus der http-Adresse ablesen lässt:

<img src="./pics/3_google_table_8.png" width=600 style="border:1px solid black"></br>  

So, jetzt wird ein wenig sportlicher: 

Wir erzeugen einen **<u>Schlüssel</u> mit dem wir später auf die Google-Tabelle automatisch/"von außen" zugreifen dürfen**. Dazu wechseln wir zu [GoogleAPIs](https://console.developers.google.com) unter der Adresse https://console.developers.google.com und müssen die Nutzungsbedingungen akzeptieren:

<img src="./pics/3_google_credentials_01.png" width=600 style="border:1px solid black"></br> 
<img src="./pics/3_google_credentials_02.png" width=600 style="border:1px solid black"></br> 

Dann suchen wir dort in der "Bibliothek" die "Google Sheets API" und aktivieren sie:

<img src="./pics/3_google_credentials_03.png" width=600 style="border:1px solid black"></br> 
<img src="./pics/3_google_credentials_04.png" width=600 style="border:1px solid black"></br> 
<img src="./pics/3_google_credentials_05.png" width=600 style="border:1px solid black"></br> 

Anschließend erstellen wir das "Projekt", das diesen Zugriff nutzen können soll. Natürlich soll es "diy-iot2ds" heißen:

<img src="./pics/3_google_credentials_06.png" width=600 style="border:1px solid black"></br> 
<img src="./pics/3_google_credentials_07.png" width=600 style="border:1px solid black"></br> 

Nun müssen wir das ganze "final" aktivieren:

<img src="./pics/3_google_credentials_08.png" width=600 style="border:1px solid black"></br> 

Aber ohne Anmeldesdaten (sogenannte credentials) geht natürlich (und glücklicherweise) nichts. 
Auf den nächsten Screens können wir sie uns besorgen und müssen sie anschließen spezifizieren:

<img src="./pics/3_google_credentials_09.png" width=600 style="border:1px solid black"></br> 

- Verwendung der "Google Sheets API" 
- über "Andere Nicht-Benutzeroberfläche" 
- mit Zugriff auf die "Anwendungsdaten", 
- wobei wir keine App Engine oder Compute Engine verwenden ("Nein, ich verwende sie nicht")

<img src="./pics/3_google_credentials_10.png" width=600 style="border:1px solid black"></br> 

Dann legen wir die eigentlichen die Anmeldedaten festlegen:

- "Name des Dienstkontos" gerne mal wieder als "diy-iot2ds" mit der
- "Rolle" "Bearbeiter" (aus dem Untermenü "Projekt") mit dem
- "Schlüsseltyp" "JSON"

<img src="./pics/3_google_credentials_11.png" width=600 style="border:1px solid black"></br> 
<img src="./pics/3_google_credentials_12.png" width=600 style="border:1px solid black"></br> 

Der erforderliche **"Schlüssel" (eine Datei im sog. "JSON"-Format) wurde erstellt und automatisch heruntergeladen und liegt im Ordner "Downloads" des Raspberry**.

<img src="./pics/3_google_credentials_13.png" width=600 style="border:1px solid black"></br> 

Nun erlauben wir zu guter letzt diesem "Nutzer" (diy-iot2ds@GMAIL-ADRESSNAME.iam.gserviceaccount.com) wieder in den Google Tabellen unter "Freigeben"
mit der Google Tabelle zu sprechen (lesen & schreiben):

<img src="./pics/3_google_credentials_14.png" width=600 style="border:1px solid black"></br> 

<a id='chapter_3-2'></a>
### 3.b Anschließen des Sensors

Der Sensor wird gleich an die Steckplätze des Raspberry angeschlossen. Damit der Raspberry mit den Steckplätzen sprechen kann müssen wir das aver zunächst im Hauptmenü (Beere oben links) im Punkt "Einstellungen"/"Raspberry Pi Konfiguration" aktivieren:

</br><img src="./pics/3_sensor_1.png" width=600 style="border:1px solid black">
</br> 
</br><img src="./pics/3_sensor_2.png" width=600 style="border:1px solid black">
</br> 

Dann schalten wir den Raspberry **aus (und stecken ihn vom Netzteil ab), um den Sensor festzuklemmen** (das Herunterfahren wird übrigens auch benötigt, um die veränderten Einstellungen zu aktivieren).  

Die Kabelverbindungen herzustellen ist etwas fummelig. Aus dem Kabelsortiment brauchen wir ein Bündel von vier Kabeln, in die man Pins "hereinstecken" kann.

<img src="./pics/3_cable.png" width=600 style="border:1px solid black"></br>  

Dann verbinden wir die Seite des Sensors, an der nur 4 Pins sind, mit den Kabeln:

<img src="./pics/3_cable_to_sensor.png" width=600 style="border:1px solid black"></br>  

Wir gucken genau auf die "Kurzbezeichnungen" auf der Platine des Sensors, merken uns jeweils genau die Kabelfarbe und verbinden die anderen Kabelenden nach folgendem Schema mit den entsprechenden Pins auf dem Raspberry:

<img src="./pics/3_wireing.png" width=600 style="border:1px solid black"></br>  
<img src="./pics/3_cable_to_raspi.png" width=600 style="border:1px solid black"></br>  

Das Ganze soll stabil sein. Aber bitte keine rohe Gewalt ausüben: die kleinen Pins könnten auch schon mal abbrechen.

Das war nun manuell-handwerklich aber auch der frickeligste Teil...

<a id='chapter_3-3'></a>
### 3.c Download und Konfiguration der Software für den Raspberry

Um die Software, die dafür sorgt, das der Raspberry sowohl mit dem Sensor, als auch mit Google sprechen kann, herunterzuladen, "clonen" wir dieses Github-Repository auf den Desktop des Raspberry. 

Dazu machen wir zunächst einen Terminal auf (schwarzes Fenster-Symbol oben links auf dem Raspberry-Bildschirm) und geben `cd Desktop` (+ `Enter`, sonst passiert nichts) für den Wechsel ins Desktop-Verzeichnis ein:

<img src="./pics/3_software_01.png" width=600 style="border:1px solid black"></br> 

Dann geben wir `git clone https://github.com/birds-on-mars/diy-iot2ds` ein, wodurch der gesamte Inhalt dieses Repos in einen Ordner auf dem Desktop des Raspberry kopiert wird:

<img src="./pics/3_software_02.png" width=600 style="border:1px solid black"></br> 
<img src="./pics/3_software_03.png" width=600 style="border:1px solid black"></br> 

Weiterhin werden wir ein paar Bibliotheken brauchen, damit die heruntergeladene Programme funktionieren und Sensor und Google-Cloud sprechen können. Dazu geben wir 

- `sudo apt-get update`
- `sudo apt-get install -y python-smbus i2c-tools`
- `pip install --upgrade google-api-python-client oauth2client httplib2`

in ein Terminalfenster ein.

<img src="./pics/3_software_03a.png" width=600 style="border:1px solid black"></br> 

Aus dem Ordner "Downloads" verschieben wir nun den vorhin kreierten "Schlüssel" in das Unterverzeichnis "src" des "diy-iot2ds"-Ordners auf dem Desktop:

<img src="./pics/3_software_04.png" width=600 style="border:1px solid black"></br> 

Durch Doppelklick auf "push_data_to_google_sheet.py" (auch im Ordner "Desktop/diy-iot2ds/src") öffnet sich das entsprechende Python-Script in der auf dem Raspberry installierten "Thonny"-Programmierumgebung

<img src="./pics/3_software_04a.png" width=600 style="border:1px solid black"></br>  

Zwei Dinge sind hier (jeweils hinter dem `=`-Zeichen zu ergänzen:

- Der Name des "Schlüssel"-/"Credential"-Files (soetwas in der Art "diy-iot2ds-....json")
- Die ID der Google Tabelle (s. oben, dort wo wir die Tabelle vorbereitet haben) (die längliche Zahlen und Buchstabenreihe)

<img src="./pics/3_software_05.png" width=600 style="border:1px solid black"></br> 

Nun speichern wir das modifizierte Skript (Button "Save").

Wir müssen auch überprüfen, ob die "pins"  wie erwartet sind (Adressen der Steckverbindungen des Sensors mit dem Raspberry).

Dazu geben wir im Terminal `i2cdetect -y 1` ein:

<img src="./pics/3_software_05a.png" width=600 style="border:1px solid black"></br>  

Sollte da `77` zu sehen sein, ist alles schon fein. Sollte da was anderes zu sehen sein (z.B. `76`), so doppelklicken wir nun auf "bme280.py" und ändern diese Nummer und speichern die Datei dann (alles wie gerade "push_data_to_google_sheet.py"):

<img src="./pics/3_software_05b.png" width=600 style="border:1px solid black"></br>  


Jetzt (die Spannung steigt, die Trommeln wirbeln) gucken wir, ob das Skript läuft, indem wir im Termninal mit `cd Desktop/diy-iot2ds/src` in unser Skript-Verzeichnis gehen und dort `python push_data_to_google_sheet.py` eingeben:

<img src="./pics/3_software_06.png" width=600 style="border:1px solid black"></br> 

Hat's funktioniert? Zeigt sowohl der Terminal, als auch die Google-Tabelle die Daten an?  
**Es hat geklappt!!**

Wir wollen nun erreichen, dass der Raspberry - einfach beim Anschalten und ohne Befehlseingabe und ohne dass Tastatur, Maus und Bildschirm angeschlossen sein müssen - startet und dauerhaft alle paar Sekunden ausführt. Dazu müssen wir noch einen sogenannten "cronjob" einrichten. Im Terminal geben wir dafür `crontab -e` ein und geben dort in eine neue Zeile `@reboot (cd /home/pi/Desktop/diy-iot2ds/src ; python stream_weather_data.py)`:

<img src="./pics/3_cronjob_1.png" width=600 style="border:1px solid black"></br> 
<img src="./pics/3_cronjob_1.png" width=600 style="border:1px solid black"></br> 

*Sollten wir gefragt werden, welcher Editor es zum Erstellen des cronjobs es sein soll, nehmen wir einfach "nano" (Option 2 - auch Vorschlag des Systems).*

Und speichen und schließen mit `Strg-O` (oder `control-O`), `Enter` und `Strg-X` (oder `control-X`).

Jetzt können wir den Raspberry ausschalten, alles abklemmen, ihn irgendwohin in Reichweite des WLAN stellen, an Strom anschließen, einschalten und **fertig ist unser IoT-Gerät, das mit der Cloud spricht!**

<a id='chapter_4'></a>
## Ein wenig Data Science...

So, super, jetzt steht unser Raspberry mit dem Sensor irgendwo in Reichweite des WLAN, surrt vor sich hin und ... nun?

Nun können wir an unseren "normalen" Computer gehen, uns bei unserem Google-Account einloggen, die Tabelle in GDrive aufmachen und uns freuen, dass etwa alle 10 Sekunden ein neuer Datensatz mit Zeit-, Temperatur-, Luftdruck- und Luftfeuchtigkeitsangabe "hereintickert". Ein Gefühl der Befriedigung macht sich bereit, aber irgendwie könnte es bunter und interessanter sein... kann man eigentlich noch Spannenderes mit den Daten machen, als nur diese Daten zu bewundern?

Klaro: dazu klicken wir diesen Link:

**GITHUB-LINK**

