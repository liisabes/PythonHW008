import output1

def Delete():

    output1.OutputAll()

    deleteElem = input("Введите строку для удаления: ")

    with open("file.txt", "r") as file:
        lines = file.readlines()
    with open("file.txt", "w") as file:
        for line in lines:
            if line.strip("\n") != deleteElem:
                file.write(line)

    output1.OutputAll()