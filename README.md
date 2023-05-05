# Blackjack harjoitin

Sovellus on peli, jota pelataan kuin perinteistä blackjackia. 

## Säännöt
Blackjack on korttipeli, jossa tavoitteena on saada pelikäsi, jolla voittaa jakajan joko siten, että pelaajan käden pistemäärä on lähempänä kahtakymmentäyhtä kuin jakajan, tai siten, että jakajan käden pistemäärä menee yli kahdenkymmenenyhden. 

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/maijarislakki/ot-harjoitustyo/blob/master/seurapeli/dokumentaatio/vaatimusmaarittely.md)

[Työkirjanpito](https://github.com/maijarislakki/ot-harjoitustyo/blob/master/seurapeli/dokumentaatio/tyokirjanpito.md)

[Changelog.md](https://github.com/maijarislakki/ot-harjoitustyo/blob/master/seurapeli/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/maijarislakki/ot-harjoitustyo/blob/master/seurapeli/dokumentaatio/arkkitehtuuri.md)


## Asennus
1. Asenna tarvittavat riippuvuudet:
poetry install
2. Suorita alustava toimenpide:
poetry run invoke build
3. Käynnistä sovellus:
poetry run invoke start
Komento "poetry run invoke start" tulee suorittaa kansiossa "seurapeli".

## Pylint
poetry run invoke lint

## Testikattavuus
poetry run invoke coverage-report

## testaus
poetry run invoke test
