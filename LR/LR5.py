'''
Лабораторная работа 5

1. Загрузить данные (ex1data.csv) из csv-файла в скрипт с помощью метода read_csv модуля pandas.

2. Используя метод plot или scatter, визуализируем данные, считанные из файла.

3. Разберемся с объектом subplot и нарисуем на этом же графике линию, «соответствующую» данным,
считанным из файла. Пусть эта будет линия, соответствующая графику функции y = 2*x-10.

4. Используя метод polyfit из библиотеки scipy получите значения коэффициентов (аналогично было
сделано в конспекте лекции) для модели линейной регрессии (степень полинома = 1)

5. Предскажите значения целевого параметра при значениях x = [2.225, 17.5, 25].

6. Еще раз визуализируйте графики из пункта 2, но дополнительно нанесите график с параметрами
модели, полученными с помощью polyfit.

'''

import numpy
import matplotlib.pyplot as plt
import pandas
import scipy as sp


def error(f, x, y):

    """
     Векторное вычисление суммы квадратов отклонений значений функции
     от известных значений целевого параметра (y).
    """

    return numpy.sum((f(x) - y) ** 2)


def line(x):
    return (2*x - 10)


def draw_graph(x, y):

    """
    Рисование графика функции.
    """

    plt.scatter(x, y, s=5)

    y_line = [line(x_i) for x_i in x]
    plt.plot(x, y_line, linewidth=2.0, color='r')

    # polyfit подбирает коэффициенты модели
    f1p, residuals, rank, sv, rcond = numpy.polyfit(x, y, 1, full=True)
    f1 = sp.poly1d(f1p)
    x_pred = [2.225, 17.5, 25]
    y_pred = [f1(x_i) for x_i in x_pred]
    print('Предсказанные значения от x = [2.225, 17.5, 25]: ', y_pred)
    print(f"{error(f1, x, y):.5}")
    fx = numpy.linspace(min(x), max(x), 500)
    plt.plot(fx, f1(fx), linewidth=2.0, color='g')

    plt.scatter(x_pred, y_pred, s=40, color='orange')

    # plt.autoscale(tight=True)
    # plt.grid(True, color='0.75')

    plt.show()
    plt.savefig("LR5.png")

def transform_data(data):

    """
    Распределение данных по двум векторам (одномерным массивам)
    """

    x = data['first'].to_list()
    y = data['second'].to_list()

    return x, y


if __name__ == '__main__':

    data = pandas.read_csv('ex1data1.csv', names=['first', 'second'])
    x, y = transform_data(data)
    draw_graph(x, y)

