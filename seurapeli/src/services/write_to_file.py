def write_to_file(data):
    with open('src/high_score_file.txt', "r") as file:
        old_content = file.read()

    # Compare the sizes of the old and new content
    if int(data) > len(old_content):
        # Open the file in write mode and overwrite the old content with the new content
        with open('src/high_score_file.txt', "w") as file:
            file.write(str(data))  # Convert data to a string before writing
        return data
    else:
        return old_content
