# Käyttöohje

## Ohjelman käynnistäminen
Ennen pelin käynnistämistä,asenna riippuvuudet komennolla:
poetry install

Tee alustustoimenpiteet komennolla:
poetry run invoke build

Nyt käynnistä ohjelma komennolla:
poetry run invoke start (tämän komennon kanssa vähän hankaluuksia niin jos peli ei aukea mene VSCodeen ja avaa se siellä).

## Pelin kulku

Näytöllä on kolme ruutua ja niitä klikkaamalla peli suorittaa eri toimintoja.
Jos haluat nostaa kortin paina "jatketaanko peliä?" ruutua. Jos haluat katsoa kortit/lopettaa kierroksen niin paina: "Katsotaanko kortit?". Jos haluat aloittaa kierroksen alusta ilman katsomatta kortteja paina: "Aloitetaanko alusta", jolloin et näe kumpi on voittanut.


## Ohjelman sulkeminen

Sulje ohjelma painamalla oikeassa yläkulmassa olevaa ruksia.
