import numpy as np
import math

"""поиск определителя"""
# a = [[3, -1, 0], [2, 1, -1], [1, 5, 4]]
# print(np.linalg.det(a))
"""создание массива"""
# import numpy as np
#
#
# def snake(m, n):
#     matrix = np.arange(1, m * n + 1).reshape(m, n)
#
#     for i in range(m):
#         if i % 2 == 1:
#             matrix[i] = matrix[i][::-1]
#
#     return matrix
# print(snake(3, 4))

"""какая то фигня которая читает и вытаскивает инфу с файла"""
# import pandas as pd
#
# df = pd.read_csv('penguins.csv')
# df_cleaned = df.dropna()
# features = df_cleaned[['bill_length_mm', 'bill_depth_mm']]
# features_array = np.array(features)
#
#
# def euclidean_distance(point1, point2):
#     return np.sqrt(np.sum((point1 - point2) ** 2))
#
#
# def find_k_nearest_neighbors(features_array, n, k):
#     if n < 0 or n >= len(features_array):
#         raise ValueError("Номер строки n выходит за пределы диапазона данных")
#     target_point = features_array[n]
#     distances = []
#     for i, point in enumerate(features_array):
#         if i != n:
#             dist = euclidean_distance(target_point, point)
#             distances.append((dist, i))
#     distances.sort(key=lambda x: x)
#     k_nearest = distances[:k]
#     nearest_indices = [idx for dist, idx in k_nearest]
#     nearest_neighbors = features_array[nearest_indices]
#     return nearest_neighbors
#
#
# n = int(input())
# k = int(input())
# nearest_neighbors = find_k_nearest_neighbors(features_array, n, k)
# for neighbor in nearest_neighbors:
#     print(neighbor)
