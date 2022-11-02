import re
import math
import random

# Question 1
def matrix_transpose(matrix):
    transposed = []
    for i in range(len(matrix)):
        transposed.append([])
        for j in range(len(matrix[i])):
            transposed[i].append(matrix[j][i])
    return transposed

# Question 2
def matrix_transpose_lc(matrix):
    transposed = [[matrix[j][i] for j in range(len(matrix[i]))] \
        for i in range(len(matrix))]
    return transposed

# Question 3
def range_sqrt(start, stop, step=1):
    return [math.sqrt(n) for n in range(start, stop, step)]

def range_cos(step_size):
    return [math.cos(3 * i/step_size) for i in range(0, step_size+1)]

# Question 4
def gen_rand_matrix(n):
    return [[random.randrange(11) for _ in range(n)] for _ in range(n)]

# Question 5
def create_stats(file):
    stats_dict = {}
    input_file = open(file, "r")
    content = input_file.read()
    word_list = content.split(" ")

    for word in word_list:
        if (word in stats_dict):
            stats_dict[word] += 1
        else:
            if len(word) >= 5:
                stats_dict[word] = 1

    input_file.close()
    return stats_dict

def get_stats_from_dict(stats_dict):
    for k, v in stats_dict.items():
        if len(k) >= 5:
            print(k)

if __name__ == "__main__":
    mat1 = [[9, 4, 6], [0, 7, 7], [3, 7, 6]]
    mat2 = [[7, 9, 7, 1, 9], [0, 4, 7, 8, 5], [3, 6, 5, 6, 8], [9, 0, 3, 0, 8], [9, 6, 7, 6, 7]]
    print(matrix_transpose(mat1) == matrix_transpose_lc(mat1))
    print(matrix_transpose(mat2) == matrix_transpose_lc(mat2))
    print(range_sqrt(1, 101))
    print(range_cos(100))
    print(gen_rand_matrix(5))
    print(gen_rand_matrix(10))
    print(create_stats("sampleFile"))
    get_stats_from_dict(
        {'color': 1, 'fruit': 3, 'pet': 2}
    )