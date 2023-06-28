def write_to_file(data):
    with open('src/high_score_file.txt', "r") as file:
        old_content = file.read()

    old_content = int(old_content) if old_content else 0

    if int(data) > old_content:
        with open('src/high_score_file.txt', "w") as file:
            file.write(str(data))
        return data
    else:
        return old_content
