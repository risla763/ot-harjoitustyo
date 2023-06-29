import pygame

def write_zero_to_file():
    """This method writes 0 to be the default high score."""
    file = open("src/high_score_file.txt", "w")
    
    
    file.write("0")
    
    
    file.close()



