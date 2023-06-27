"""This method fetches what is inside the high_score_file"""
def get_high_score():
    with open("src/high_score_file.txt", "r") as file:
        high_score = int(file.read())
    return high_score

        