# Ohjelmistotekniikka harjoitustyö

Olen tekemässä *japaninkielen* hiragana-kirjoitusmerkkien harjoittelua varten sovelluksen, joka on koodattu pythonilla ja sen saa avattua **lokaalisti** koneelle komentoriviltä.

## Asennus
Asenna tarvittavat riippuvuudet "hiragana_app" nimisen kansion sisällä: poetry install
Käynnistä sovellus: "poetry run invoke start" tulee suorittaa kansiossa "hiragana-app" jos ei halua käyttää invokea niin pelin saa myös päälle "hiragana-app" nimisessä kansiossa: poetry run python src/index.py

## testit

Testit voidaan ajaa sovelluksessa komennolla: 'poetry run invoke tests' ja testeistä tehdyn raportin voi saada: 'poetry run invoke coverage-report'.
Raportin saa auki esimerkiksi: 'xdg-open htmlcov/index.html'.

pylint ajetaan komennolla: poetry run pylint src



## Ohjelmointikieli

Python ja tietokanta SQL

## Vaatimusmäärittely

[Linkki vaatimusmäärittelyyn](https://github.com/risla763/ot-harjoitustyo/blob/main/hiragana-app/dokumentaatio/vaatimusmaarittely.md)

## Laskarit

[Linkki viikottaisiin laskareihin](https://github.com/risla763/ot-harjoitustyo/tree/main/laskarit)

## Työkirjanpito

[Linkki työkirjanpitoon](https://github.com/risla763/ot-harjoitustyo/blob/main/hiragana-app/dokumentaatio/tyokirjanpito.md)

## Changelog
[Linkki changelogiin](https://github.com/risla763/ot-harjoitustyo/blob/main/hiragana-app/dokumentaatio/changelog.md)

## Arkkitehtuuri

[Linkki arkkitehtuuriin](https://github.com/risla763/ot-harjoitustyo/tree/main/hiragana-app/dokumentaatio/arkkitehtuuri.md)
