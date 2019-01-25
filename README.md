Toteutus löytyy verkosta osoitteesta https://tsoha-senaatti.herokuapp.com/

# Senaatti webapp

Sanalla "Senaatti" tarkoitetaan keskustelevaa kokousta. Kokouksen (äänestyksen) alkuunpanija valitsee senaatin jäsenet tai vaihtoehtoisesti jättää äänestykseen osallistumisen avoimeksi. Mahdollisia ääniä ovat 👍 , 👎 tai 🤞 (*neutraali* ääni).

## Ominaisuudet

Käyttäjä voi lukea järjestelmään tallennettuja avoimia senaatteja, sekä niitä senaatteja joissa hän on itse jäsen. Senaatti on aktiivinen kunnes kaikki sen jäsenet ovat äänestäneet, tai avoimissa senaateissa kunnes senaatin alkuunpanijan valitsema määrä ääniä on tallennettu. Kun senaatti ei ole enään aktiivinen, se arkistoidaan jolloin siitä ei voi enään keskustella, eikä sen lopputulokseen osallistua taikka vaikuttaa. [Lisää ominaisuuksia user stories- dokumentissa](documentation/userstories.md)

## Toimintoja

* Kirjautuminen
* Senaatin alkuunpano, otsikon valinta, osallistujien valinta
* Senaattien näyttäminen eri kriteerein
* Aktiivisessa senaatissa äänestäminen
* Aktiivisessa senaatissa keskustelu
* Senaatin poistaminen
* Arkistoidun senaatin lopputuloksen katselmointi

## Tietokanta

Käytössä on relaatiotietokanta. [Tietokantakaavio löytyy täältä](documentation/database_uml.png)
