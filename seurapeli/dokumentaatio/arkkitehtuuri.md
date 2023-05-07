# Arkkitehtuuri
## Rakenne

Koodin pakkausrakenteeseen kuuluu kansio nimeltä "Services", joka sisältää sovelluksen logiikan. Tämän kansion sisällä on myös kaksi muuta kansiota, mitkä ovat "ui", joka sisältää käyttöliittymän ja kaiken "piirtämisen" sekä "entities" , joka sisältää sovelluksen käyttämiä png-tiedostoja.

(tähän kuva)

## Käyttöliittymä

Sovelluksen käyttöliittymä sisältää vain yhden näkymän. Pelin auetessa näytöllä näkyy pelin aloitustilanne. Luokka "Main" vastaa näytön koon ja värin määrittelystä ja sen piirtämisestä. Kuitenkin Ui nimisessä kansiossa olevat luokat ja metodit vastaavat kaiken muun piirtämisestä. 

## Sovelluslogiikka

Pelin logiikasta vastaa luokat ja metodit, jotka sijaitsevat kansion "services" sisällä. Pelin alustuksesta vastaa main_game_loop.py sijaitsevassa tiedostossa oleva Main-luokka, joka kutsuu erilaisia metodeja riippuen siitä, mitä käyttäjä päättää tehdä. 
Pelin alustamisessa Main-luokka myös kutsuu Deck-luokkaa, jossa tapahtuu kaikki korttipakkaan liittyvä logiikka, kuten sen sekoittaminen ja jakajan sekä pelaajan nostamien korttien summien kirjanpito.

Deck luokan metodeja ovat esimerkiksi: 
  next_card
  next_card_dealer
  count
  count2
  see_cards
  round_ends
Näistä metodeista kahta ensimmäistä kutsutaan Main luokasta, kun käyttäjä painaa "Jatketaanko peliä?" nimistä nappia. Tällöin koodissa siirrytään next_card nimiseen metodiin, jossa pelaajalle jaetaan uusi kortti. Next_card_dealer taas jakaa jakajalle kortin, jota kutsutaan Main luokassa olevasta laskurista riippuen.

Count ja count2 metodit sen sijaan pitävät kirjaa jakajan ja pelaajan pisteistä. Näitäkin kutsutaan Main luokasta.

See_cards ja round_ends metodit liittyvät kierroksen loppumiseen ja näitä kutsutaan Main luokasta, kun käyttäjä painaa näytöllä ruutua: "lopetetaanko peli?" tai peli loppuu siihen, että pelaajan korttien yhteissumma ylittää 21. 

(joku kuva tähän?)

## Päätoiminnallisuus

Tässä kuvaan osaa sovelluksen logiikasta sekvenssikaavioina.

### Pelin jatkaminen
Kun pelaaja haluaa jatkaa peliä ja painaa näytöllä olevaa ruutua, jossa lukee: "Jatketaanko peliä?" niin koodi etenee näin: 
(kuva)
Kun pelaaja klikkaa näytöllä olevaa: "Jatketaanko peliä" tekstiä niin Main luokassa olevassa loopissa koodi siirtyy if-else lausekkeeseen, jossa koodi kutsuu metodeita draw_next, count, count2, next_card_dealer ja draw_next, jos count on 3. Kaikki näistä sijaitsee Deck luokassa paitsi draw_next metodi. Draw_next metodi saa parametrikseen muuttujat, jotka määrittelevät kortin paikan näytöllä. Tämän avulla näytöle piirtyy kortti. Samalla kun kutsutaan next_card_dealer niin sen metodin sisällä on toinen if-else-lauseke, joka määrittelee mihin jakajan kortti piirretään näytölle.



https://github.com/maijarislakki/ot-harjoitustyo/blob/master/seurapeli/dokumentaatio/IMG_20230418_230849.jpg
