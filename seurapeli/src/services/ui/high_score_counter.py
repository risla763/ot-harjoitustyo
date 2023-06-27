def high_score(high_scoree):
    """this returns the high score"""
    with open("high_score.txt") as file:
        if high_scoree > current_high_score: #current hae sieltä vaikka file.read()
            high_score = file.write(high_scoree)
            file.close()
        else:
            pass
    #pitäisikö tässä jo mennä piirtämis metodiin?
    return high_score
#tässä se kirjoittaa high_scoree nimisen asian sinne ja se on korkein score
#TÄHÄN SE ETTÄ VERTAILEE HIGH SCOREA JOKA ON ALUSSA NOLLA NIIN SIIHEN SCOREN JOKA ON PELAAJALLA PLAYER_SCORE KUN KIERRS LOPPUU
#laita sillee että kun pakka loppuu? niin sitten tää ilmestyy näytölle ja tee oma metodi draw high_score 