def OutputAll():
    with open('file.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line)