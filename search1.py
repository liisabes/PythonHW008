# def Search(data):
#     with open('file.txt', 'r', encoding='utf-8') as file:
#         flag = False
#         for line in file:
#             if data in line:
#                 print(line)
#                 flag = True
#         if flag == False:
#             print("\nЗапись не найдена\n")
def Search(data):
    with open('file.txt', 'r', encoding='utf-8') as file:
        flag = False
        for line in file:
            if data in line:
                print(line)
                return line