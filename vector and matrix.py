import math
"""вектора"""

def scalar_vector_multiplication():
    x = input()
    x = x.split(",")
    y = input()
    y = y.split(",")
    sm = []
    if len(x) == len(y):
        for i in range(len(x)):
            sm.append(float(x[i]) * float(y[i]))
        return sum(sm)
    else:
        return "ошибка значений"

def euclidean_distance():
    sm = []
    x = input()
    x = x.split(",")
    y = input()
    y = y.split(",")
    if len(x) == len(y):
        for i in range(len(x)):
            sm.append((float(x[i]) - float(y[i])) ** 2)
        s_sm = sum(sm)
        return math.sqrt(s_sm)
    else:
        return "ошибка значений"

def manhattan_distance():
    x = input()
    x = x.split(",")
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







