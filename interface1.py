# Задача 38: 
# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных

import input1
import output1
import search1
import change1
import delete1

while True:
    chiose = int(input("Введите действие:\n0 - Выйти из программы \n1 - Добавить\n2 - Вывести\n3 - Поиск\n4 - Изменить\n5 - Удалить\n"))
    match chiose:
        case 0:
            break
        case 1:
            input1.Input(input("Введите имя: "), input("Введите номер: "))
        case 2:
            output1.OutputAll()
        case 3:
            search1.Search(input("Введите элемент для поиска: "))
        case 4:
            change1.Change()
        case 5:
            delete1.Delete()