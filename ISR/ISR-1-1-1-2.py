'''

Инвариантная самостоятельная работа

1.1. Разработка скрипта, вычисляющего статистические показатели (среднее значение, дисперсия,
     среднее квадратичное отклонение) для данных, считанных из CSV-файла.

1.2. Осуществить рефакторинг (модификация) скрипта, вычисляющего статистические показатели для данных,
     считанных из CSV, с использованием библиотеки научных вычислений numpy.

1.3. На основе данных, предоставленных преподавателем, реализовать отображение данных на точечной
     диаграмме с помощью библиотеки matplotlib. Создать модель (квадратичная функция) для предсказания
     новых данных и нанести график этой функции на точечную диаграмму.
     Вычислить отклонение данных модели от реальных данных.

1.4. Формирование отчета по выполненной самостоятельной работе и публикация его в портфолио.

'''

# 1.1
import csv
import numpy

from math import sqrt


def mean_quadratic_deviation(data):
    """
    Среднее квадратичное отклонение данных из переданного списка.
    :param data:
    :return:
    """

    m_q_deviation = sqrt(dispersion(data))

    return m_q_deviation


def dispersion(data):
    """
    Дисперсия данных из переданного списка.
    :param data:
    :return:
    """

    data_average = average(data)

    data_for_dispersion = [(x_i - data_average) ** 2 for x_i in data]
    sum_data = sum(data_for_dispersion)
    data_dispersion = sum_data/(len(data_for_dispersion))

    return data_dispersion


def average(data):
    """
     Среднее значение данных из переданного списка.
    :param data:
    :return: average
    """

    sum_data = sum(data)
    count_data = len(data)

    data_average = sum_data/count_data

    return data_average


def csv_reader(file_csv, col_num):
    """
        Функция для считывания данных из csv файла.
    """
    reader = csv.reader(file_csv, delimiter=';')
    data = []
    for line in reader:
        data += [float(line[col_num - 1].replace(',', '.'))]
    return data


if __name__ == "__main__":
    csv_path = "ISR.csv"  # Приморский район
    col_num = 1

    with open(csv_path, encoding='utf-8', newline='') as f_obj:
        data = csv_reader(f_obj, col_num)

    print('Среднее значение: ', average(data))
    print('Дисперсия: ', dispersion(data))
    print('Среднее квадратичное отклонение: ', mean_quadratic_deviation(data))
    
    # 1.2
    print('Среднее значение: ', numpy.mean(data))
    print('Дисперсия: ', numpy.var(data))
    print('Среднее квадратичное отклонение: ', numpy.std(data))
