# Käyttöohje

## Ohjelman käynnistäminen
Ennen pelin käynnistämistä, asenna riippuvuudet komennolla:

*poetry install*

Tee alustustoimenpiteet komennolla:

*poetry run invoke build*

Nyt käynnistä ohjelma komennolla:

*poetry run invoke start* (tämä komento suoritetaan seurapeli nimisessä kansiossa)
## Pelin kulku

Näytöllä on kolme ruutua ja niitä klikkaamalla peli suorittaa eri toimintoja.
Jos haluat nostaa kortin paina "jatketaanko peliä?" ruutua. Jos haluat katsoa kortit/lopettaa kierroksen niin paina: "Katsotaanko kortit?". Jos haluat aloittaa kierroksen alusta ilman katsomatta kortteja paina: "Aloitetaanko alusta", jolloin pisteitä ei lasketa.
pelin käyttäjän kortit tulevat vasemmalle puolelle ruutua ja jakajan kortit tulevat oikealle puolelle ruutua. Jokaisen kierroksen päätyttyä näytölle myös ilmestyy pistelaskuri, joka näyttää kumpi on voittanut enemmän kierroksia. Pistelaskuri ei kuitenkaan näy koko ajan näytöllä.

Peli käyttää yhtä luotua pakkaa kunnes se loppuu. Kun pakka loppuu, niin kaikki arvot nollaantuvat kuten laskuri, joka pitää kirjaa siitä kumpi on voittanut enemmän kierroksia. Tässä myös on bugi, joka ilmenee siten että näyttö muuttuu mustaksi ensimmäisellä kierroksella uudella pakalla, mutta peli muuttuu normaaliksi kun painaa "Aloitetaanko alusta?" laatikkoa.


## Ohjelman sulkeminen

Sulje ohjelma painamalla oikeassa yläkulmassa olevaa ruksia.
