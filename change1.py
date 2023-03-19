import output1

def Change():

    output1.OutputAll()

    elemToReplase = input("Введите элемент, который меняете: ")
    replaseElem = input("Введите элемент, на который меняете: ")
    
    with open ('file.txt', 'r') as file:
        data = file.read()

    replaseData = data.replace(elemToReplase, replaseElem)

    with open ('file.txt', 'w') as file:
        file.write(replaseData)

    output1.OutputAll()