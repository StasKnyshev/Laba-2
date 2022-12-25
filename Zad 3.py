import numpy as np

print()
n = int(input('Введите кол-во строк матрицы: '))
stolb = int(input('Введите кол-во столбцов матрицы: '))
while n != stolb:
    print()
    print('Данная матрица не является квадратной, введите данные ещё раз')
    n = int(input('Введите кол-во строк матрицы: '))
    stolb = int(input('Введите кол-во столбцов матрицы: '))
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
print ()

opr = np.linalg.det(mat)
if opr == 0:
    print ('Данная матрица необратима!!! ')
else:
    print(); print('Матрица: ');print (np.array(mat)); print()
    obr = np.linalg.inv(mat)
    print(obr)