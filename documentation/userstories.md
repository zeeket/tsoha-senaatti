# User Stories - Käyttäjätarinoita

Senaatti- sivuston käyttäjä on kiinnostunut vaikuttamaan päätöksiin.

## Senaatin luojana haluan...
(INSERT INTO poll VALUES)
- Asettaa senaatille aiheen (name)
- Asettaa senaatille kuvauksen (description)
- Valita senaatin julkisuuden julkiseksi tai yksityiseksi TODO (FOREIGN KEY(group_id) REFERENCES group (id))
- Valita yksityiseen senaattiin käyttäjät
- Aloittaa senaatin
- Pysäyttää senaatin, niin että se arkistoidaan (done)
- Katsoa senaatin lopputulosta

## Senaattiin osallistujana haluan...

- Äänestää yksityisissä senaateissa joihin minut on kutsuttu (INSERT INTO poll_account_link VALUES current-user.id AS userid, poll_id as pollid)
- Äänestää julkisissa senaateissa (INSERT INTO poll_account_link VALUES current-user.id AS userid, poll_id as pollid)
- Järjestää senaatteja eri kriteerein TODO
- Katsoa senaatin lopputulosta 

## Ryhmän luojana haluan
(INSERT INTO group VALUES)
- Asettaa ryhmälle nimen (name)
- Valita ryhmän jäsenet (INSERT INTO group_account_link VALUES group_id AS group_id, account_id AS account_id...)

# Ryhmä 0 sisältää kaikki käyttäjät, eli julkiset senaatit saavat ryhmäkseen 0.
