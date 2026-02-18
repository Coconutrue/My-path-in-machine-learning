import math
import itertools

"""вектора"""

"""умножение вектора на вектор"""

def scalar_vector_multiplication():
    print("введи первый вектор:")
    x = input()
    x = x.split(",")
    print("введи второй вектор:")
    y = input()
    y = y.split(",")
    sm = []
    if len(x) == len(y):
        for i in range(len(x)):
            sm.append(float(x[i]) * float(y[i]))
        return sum(sm)
    else:
        return "ошибка значений"

"""расстояние между векторами(евклидово)"""

def euclidean_distance():
    sm = []
    print("введи первый вектор:")
    x = input()
    x = x.split(",")
    print("введи второй вектор:")
    y = input()
    y = y.split(",")
    if len(x) == len(y):
        for i in range(len(x)):
            sm.append((float(x[i]) - float(y[i])) ** 2)
        s_sm = sum(sm)
        return math.sqrt(s_sm)
    else:
        return "ошибка значений"

"""расстояние между векторами(манхетенское)"""

def manhattan_distance():
    print("введи первый вектор:")
    x = input()
    x = x.split(",")
    print("введи второй вектор:")
    y = input()
    y = y.split(",")
    sm = []
    if len(x) == len(y):
        for i in range(len(x)):
            sm.append(math.fabs(float(x[i]) - float(y[i])))
        return sum(sm)
    else:
        return "ошибка значений"


"""матрицы"""

"""умножение матрицы на вектор"""

def multiply_vector_by_matrix():
    len_m = int(input("введи количество столбцов у матрицы:"))
    matrix = []
    last_matrix = []
    print("вводи матрицу столбами(1 столбец - одна строчка(значения через пробел!):")
    for i in range(len_m):
        m = input()
        matrix.append(m.split(" "))
    vector = input("введи вектор(значения через пробел!)").split(" ")
    if len(vector) == len(matrix[0]):
        for i in range(len(matrix)):
            per = []
            for j in range(len(vector)):
                per.append(float(matrix[i][j]) * float(vector[j]))
            last_matrix.append(per)
        for l in range(len(last_matrix)):
            last_matrix[l] = sum(last_matrix[l])
        return last_matrix
    else:
        return "ошибка значений"

"""умножение матрицы на матрицу"""

def multiply_matrix_by_matrix():
    print("введите количество строк матрицы:")
    count_str = int(input())
    x = []
    print("вводите строки матрицы, значение через пробел. Одна строка - одна строчка:")
    for m in range(count_str):
        x.append(input().split(" "))
    print("введите количество столбцов второй матрицы:")
    count_str2 = int(input())
    y = []
    print("вводите столбцы матрицы, значения через пробел. Один столбец - одна строчка:")
    for n in range(count_str2):
        y.append(input().split(" "))
    last_matrix = [[], []]
    for k in range(count_str2):
        for j in range(count_str):
            per = []
            for i in range(len(x[0])):
                per.append(float(x[j][i]) * float(y[k][i]))
            last_matrix[k].append(sum(per))
    print("в списке заключается ответ. Один список - один столбец получившейся матрицы:")
    return last_matrix

"""транспонирование матриц"""

def transposition_matrix():
    print("вводите количество столбцов матрицы:")
    count_str = int(input())
    tr_matrix = []
    print("вводите столбцы матрицы. Значения через пробел. Одна строка - один столбец")
    for i in range(count_str):
        tr_matrix.append(input().split(" "))
    print("транспонированная матрица")
    for j in range(len(tr_matrix)):
        print(tr_matrix[j])

"""поиск определителя"""

def determinant_of_matrix():
    n = int(input("Введите количество строк: "))
    print("Вводите строки матрицы. Значения через пробел. Одна строчка - одна строка")
    matrix = []
    for i in range(n):
        row = list(map(float, input(f"Строка {i + 1}: ").split()))
        if len(row) != n:
            print(f"Ошибка: нужно ровно {n} чисел!")
            return
        matrix.append(row)

    def count_inversions(perm):
        """Считает число инверсий в перестановке."""
        inversions = 0
        for i in range(len(perm)):
            for j in range(i + 1, len(perm)):
                if perm[i] > perm[j]:
                    inversions += 1
        return inversions

    def sign(perm):
        """Возвращает знак перестановки: +1 если чётная, -1 если нечётная"""
        inversions = count_inversions(perm)
        return 1 if inversions % 2 == 0 else -1

    def determinant(matrix):
        """Вычисляет определитель по формуле Лейбница"""
        n = len(matrix)
        if n == 1:
            return matrix[0][0]

        total = 0
        for perm in itertools.permutations(range(n)):
            product = 1
            for row in range(n):
                col = perm[row]
                product *= matrix[row][col]
            total += sign(perm) * product
        return total

    det = determinant(matrix)
    return f"Определитель матрицы: {det}"



