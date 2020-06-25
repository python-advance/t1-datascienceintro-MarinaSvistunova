# ИСР 1.3

'''

1.3. На основе данных, предоставленных преподавателем, реализовать отображение данных на точечной
     диаграмме с помощью библиотеки matplotlib. Создать модель (квадратичная функция) для предсказания
     новых данных и нанести график этой функции на точечную диаграмму.
     Вычислить отклонение данных модели от реальных данных.

'''

import numpy
import matplotlib.pyplot as plt
import scipy as sp


def error(f, x, y):

    """
     Векторное вычисление суммы квадратов отклонений значений функции
     от известных значений целевого параметра (y).
    """

    return numpy.sum((f(x) - y) ** 2)


def draw_graph(x, y):

    """
    Рисование графика функции.
    """

    # polyfit подбирает коэффициенты модели
    f2p, residuals, rank, sv, rcond = numpy.polyfit(x, y, 2, full=True)
    f2 = sp.poly1d(f2p)
    print(f"{error(f2, x, y):.5}")

    fx = numpy.linspace(0, x[-1], 500)
    plt.plot(fx, f2(fx), linewidth=2.0, color='r')

    plt.scatter(x, y, s=5)
    plt.title('Трафик веб-сайта за последний месяц')

    plt.xlabel("время")
    plt.ylabel("запросы/час")

    plt.xticks([w * 7 * 24 for w in range(10)], ["неделя %i" % w for w in range(10)])
    plt.autoscale(tight=True)

    plt.grid(True, linestyle='-', color='0.75')
    plt.show()


def transform_data(data):

    """
    Распределение данных по двум векторам (одномерным массивам)
    :param data:
    :return:
    """

    x = data[:, 0]
    y = data[:, 1]

    x = x[~numpy.isnan(y)]
    y = y[~numpy.isnan(y)]

    return x, y


if __name__ == '__main__':

    data = numpy.genfromtxt('web_traffic.tsv', delimiter='\t')
    x, y = transform_data(data)
    draw_graph(x, y)
