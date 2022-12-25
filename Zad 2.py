import numpy as np

print ('Доступные функции: "Транспонирование", "Умножение", "Ранг"'); print ()
fun = input('Выберите функцию: ')
while fun not in ('Транспонирование', 'Умножение', 'Ранг'):
    fun = input('Данной функции не существует, введите корректную функцию: ')
print ()

if fun in ('Транспонирование','Ранг'):
    n = int(input('Введите кол-во строк матрицы (1 - 3): '))
    while n < 1 or n > 3:
        n = int(input('Введено некорректное кол-во строк, введите значение ещё раз: '))
    stolb = int(input('Введите кол-во столбцов матрицы (1 - 3): '))
    while stolb < 1 or stolb > 3:
        stolb = int(input('Введено некорректное кол-во столбцов, введите значение ещё раз: '))
    print()
    mat = []
    stroki = 1
    for i in range(n):
        print ('Введите',stolb,'элемент(а)',stroki,'-ой строки через пробел: ')
        row = input().split()
        while len(row) < stolb:
            print('В данной строке кол-во элементов меньше', stolb, ', введите строку ещё раз: ')
            row = input().split()
            while len(row) > stolb:
                print('В данной строке кол-во элементов больше', stolb, ', введите строку ещё раз: ')
                row = input().split()
        while len(row) > stolb:
            print('В данной строке кол-во элементов больше', stolb, ', введите строку ещё раз: ')
            row = input().split()
            while len(row) < stolb:
                print('В данной строке кол-во элементов меньше', stolb, ', введите строку ещё раз: ')
                row = input().split()
        stroki += 1
        for i in range(len(row)):
            row[i] = int(row[i])
        mat.append(row)
    print(); print('Матрица: ');print (np.array(mat)); print()

    if fun in ('Транспонирование'):
        trans = np.transpose(mat)
        print('Транспонированная матрица: ');print (trans)

    if fun in ('Ранг'):
        rang = np.linalg.matrix_rank(mat)
        print('Ранг данной матрицы равен:',rang)


if fun in ('Умножение'):
    n = int(input('Введите кол-во строк матрицы A (1 - 3): '))
    while n < 1 or n > 3:
        n = int(input('Введено некорректное кол-во строк, введите значение ещё раз: '))
    stolb = int(input('Введите кол-во столбцов матрицы A (1 - 3): '))
    while stolb < 1 or stolb > 3:
        stolb = int(input('Введено некорректное кол-во столбцов, введите значение ещё раз: '))
    print()

    n2 = int(input('Введите кол-во строк матрицы B (1 - 3): '))
    while n2 < 1 or n2 > 3:
        n2 = int(input('Введено некорректное кол-во строк, введите значение ещё раз: '))
    stolb2 = int(input('Введите кол-во столбцов матрицы B (1 - 3): '))
    while stolb2 < 1 or stolb2 > 3:
        stolb2 = int(input('Введено некорректное кол-во столбцов, введите значение ещё раз: '))
    print()

    while stolb != n2:
        print ('Невозможно выполнить умножение матриц - количество столбцов матрицы A должно совпадать с количеством строк матрицы B');print()
        n = int(input('Введите кол-во строк матрицы A (1 - 3): '))
        while n < 1 or n > 3:
            n = int(input('Введено некорректное кол-во строк, введите значение ещё раз: '))
        stolb = int(input('Введите кол-во столбцов матрицы A (1 - 3): '))
        while stolb < 1 or stolb > 3:
            stolb = int(input('Введено некорректное кол-во столбцов, введите значение ещё раз: '))
        print()

        n2 = int(input('Введите кол-во строк матрицы B (1 - 3): '))
        while n2 < 1 or n2 > 3:
            n2 = int(input('Введено некорректное кол-во строк, введите значение ещё раз: '))
        stolb2 = int(input('Введите кол-во столбцов матрицы B (1 - 3): '))
        while stolb2 < 1 or stolb2 > 3:
            stolb2 = int(input('Введено некорректное кол-во столбцов, введите значение ещё раз: '))
        print()

    mat = []
    stroki = 1
    for i in range(n):
        print('Введите', stolb, 'элемент(а)', stroki, '-ой строки через пробел: ')
        row = input().split()
        while len(row) < stolb:
            print('В данной строке кол-во элементов меньше', stolb, ', введите строку ещё раз: ')
            row = input().split()
            while len(row) > stolb:
                print('В данной строке кол-во элементов больше', stolb, ', введите строку ещё раз: ')
                row = input().split()
        while len(row) > stolb:
            print('В данной строке кол-во элементов больше', stolb, ', введите строку ещё раз: ')
            row = input().split()
            while len(row) < stolb:
                print('В данной строке кол-во элементов меньше', stolb, ', введите строку ещё раз: ')
                row = input().split()
        stroki += 1
        for i in range(len(row)):
            row[i] = int(row[i])
        mat.append(row)
    print(); print('Матрица A:');print (np.array(mat)); print()

    mat2 = []
    stroki2 = 1
    for j in range(n2):
        print('Введите', stolb2, 'элемент(а)', stroki2, '-ой строки через пробел: ')
        row2 = input().split()
        while len(row2) < stolb2:
            print('В данной строке кол-во элементов меньше', stolb2, ', введите строку ещё раз: ')
            row2 = input().split()
            while len(row2) > stolb2:
                print('В данной строке кол-во элементов больше', stolb2, ', введите строку ещё раз: ')
                row2 = input().split()
        while len(row2) > stolb2:
            print('В данной строке кол-во элементов больше', stolb2, ', введите строку ещё раз: ')
            row2 = input().split()
            while len(row2) < stolb2:
                print('В данной строке кол-во элементов меньше', stolb2, ', введите строку ещё раз: ')
                row2 = input().split()
        stroki2 += 1
        for j in range(len(row2)):
            row2[j] = int(row2[j])
        mat2.append(row2)
    print(); print('Матрица B:');print (np.array(mat2)); print()

    proizv = np.dot(mat, mat2)
    print('Произведение матриц A и B: '); print(proizv)