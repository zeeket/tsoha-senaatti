Toteutus löytyy verkosta osoitteesta https://tsoha-senaatti.herokuapp.com/

# Senaatti webapp

Sanalla "Senaatti" tarkoitetaan keskustelevaa kokousta. Kokouksen (äänestyksen) alkuunpanija valitsee senaatin jäsenet tai vaihtoehtoisesti jättää äänestykseen osallistumisen avoimeksi. Mahdollisia ääniä ovat 👍 , 👎 tai 🤞 (*neutraali* ääni).

## Ominaisuudet

Käyttäjä voi lukea järjestelmään tallennettuja avoimia senaatteja, sekä niitä senaatteja joissa hän on itse jäsen. Senaatti on aktiivinen kunnes kaikki sen jäsenet ovat äänestäneet, tai avoimissa senaateissa kunnes senaatin alkuunpanijan valitsema määrä ääniä on tallennettu. Kun senaatti ei ole enään aktiivinen, se arkistoidaan jolloin siitä ei voi enään keskustella, eikä sen lopputulokseen osallistua taikka vaikuttaa. [Lisää ominaisuuksia user stories- dokumentissa](documentation/userstories.md)

## Toimintoja

* Kirjautuminen & uuden käyttäjän rekisteröinti
  * Testitunnukset herokussa ovat testitunnus:testisalasana (muodossa käyttäjänimi:salasana)
* Senaatin alkuunpano, otsikon valinta, osallistujien valinta (1/3 TODO)
* Senaattien näyttäminen eri kriteerein (TODO)
* Aktiivisessa senaatissa äänestäminen (TODO)
* Aktiivisessa senaatissa keskustelu (TODO)
* Senaatin poistaminen (TODO)
* Arkistoidun senaatin lopputuloksen katselmointi (TODO)

## Tietokanta

Käytössä on relaatiotietokanta. [Tietokantakaavio löytyy täältä](documentation/database_uml.png).

Salasanoja **ei** pidetä selkokielellä tietokannassa- käytössä on [argon2-hajautusfunktio](https://en.wikipedia.org/wiki/Argon2).
