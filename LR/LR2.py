# Лабораторная работа 2

"""
Используя обучающий набор данных о пассажирах Титаника,
находящийся в проекте (оригинал: https://www.kaggle.com/c/titanic/data), визуализируйте данные:
- стоимости билетов пассажиров с помощью диаграммы рассеяния (scatterplot):
по оси X - пассажиры в порядке увеличения PassengerId, по оси Y - стоимость билетов
- проанализировать как наилучшим образом визуализировать данные о ценовом распределении билетов (предложить собственный вариант реализации после создании визуализации ниже).

 Отобразить два графика (subplot) на одном изображении (figure):
 1. График типа boxplot, на котором отобразить распределение цен билетов по классам (1, 2, 3).
 2. Столбчатую диаграмму (countplot) с распределением средних цен на билеты сгруппированным по трем портам (S, C, Q).

Сохранить получившиеся графики в файлах: result1.png, result2.png.
Настроить название графиков, подписи осей, отобразить риски с числовыми значениями на графике, сделать сетку на графике
(если необходимо для улучшения изучения данных на графике).

"""

import matplotlib.pyplot as plt
import numpy as np
import pandas
import seaborn as sns

from collections import OrderedDict

# считаем данных из файла, в качестве столбца индексов используем PassengerId
data = pandas.read_csv('train.csv', index_col="PassengerId")
prices = data['Fare']

'''
График типа boxplot, на котором отобразить распределение цен билетов по классам (1, 2, 3)
'''

# Вариант 1
first_class_list = data['Fare'].loc[data['Pclass'] == 1].to_list()
second_class_list = data['Fare'].loc[data['Pclass'] == 2].to_list()
third_class_list = data['Fare'].loc[data['Pclass'] == 3].to_list()

prices_classes = [first_class_list, second_class_list, third_class_list]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
ax.boxplot(prices_classes)
fig.savefig("boxplot_1.png")

# Вариант 2
plot = data.boxplot(by='Pclass', column=['Fare'], grid=False)
fig2 = plot.get_figure()
fig2.savefig("boxplot_2.png")
plt.close()

'''
 2. Столбчатую диаграмму (countplot) с распределением средних цен на билеты сгруппированным по трем портам (S, C, Q).
'''

embarked_list = data[['Embarked', 'Fare']].groupby('Embarked')['Fare'].mean().to_frame().reset_index()['Embarked'].to_list()
fare_list = data[['Embarked', 'Fare']].groupby('Embarked')['Fare'].mean().to_frame().reset_index()['Fare'].to_list()

lists = OrderedDict([('Embarked', embarked_list), ('Fare', fare_list)])
df = pandas.DataFrame.from_dict(lists)

fig3 = sns.countplot(x="Embarked", data=df).get_figure()
fig3.savefig("countplot.png")
