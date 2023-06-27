import pygame

def write_zero_to_file():
    # Open the file in write mode
    file = open("src/high_score_file.txt", "w")
    
    # Write "0" to the file
    file.write("0")
    
    # Close the file
    file.close()



