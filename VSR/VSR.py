'''

Вариативная самостоятельная работа

1.1. Разработка скрипта, вычисляющего произведение матриц произвольной размерности с использованием библиотеки numpy
и замер времени вычисления. Создание отчета по результатам анализа производительности.

'''

import numpy
import  random

from datetime import datetime


def random_float():
    random.seed()
    return random.random()


def time_report(function):

    def wrapped(*args):

        start_time = datetime.now()

        file = open('report.txt', 'a')
        file.write('Первая матрица:\n')
        file.write(str(args[0]))
        file.write('\nВторая матрица:\n')
        file.write(str(args[1]))
        result = function(*args)
        end_time = datetime.now() - start_time
        file.write('\nВремя выполнения:\n')
        file.write(str(end_time))
        file.write('\n\n')
        file.close()

        return result

    return wrapped


def read_matrix():

    matrix = []

    lines, cols = list(map(int, input('Введите размерность матрицы (строки столбцы): ').split()))

    for line in range(lines):
        new_line = []
        for col in range(cols):
            new_line += [random_float()]  # float(input())
        matrix += [new_line]

    return matrix


@time_report
def multiply_matrix(matrix1, matrix2):

    if len(matrix1[0]) == len(matrix2):
        print('Произведение матриц:\n', numpy.dot(matrix1, matrix2))
    else:
        print('Размерность матриц не позволяет произвести умножение данных матриц.')


if __name__ == "__main__":

    matrix1 = numpy.array(read_matrix(), float)
    matrix2 = numpy.array(read_matrix(), float)

    print('Первая матрица:\n', matrix1)
    print('Вторая матрица:\n', matrix2)

    multiply_matrix(matrix1, matrix2)
