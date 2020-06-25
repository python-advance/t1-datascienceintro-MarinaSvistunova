# Лабораторная работа 1
"""
Используя обучающий набор данных о пассажирах Титаника, находящийся в проекте (оригинал: https://www.kaggle.com/c/titanic/data), найдите ответы на следующие вопросы:

1. Какое количество мужчин и женщин ехало на пароходе? Приведите два числа через пробел.

2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.

3. Посчитайте долю погибших на пароходе (число и процент)?

4. Какие доли составляли пассажиры первого, второго, третьего класса?

5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).

6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
1) возрастом и параметром survival;
2) полом человека и параметром survival;
3) классом, в котором пассажир ехал, и параметром survival.

7. Посчитайте средний возраст пассажиров и медиану.
8. Посчитайте среднюю цену за билет и медиану.

9. Какое самое популярное мужское имя на корабле?
10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?

"""

import pandas  # импортирование библиотеки для считывания данных

# считаем данных из файла, в качестве столбца индексов используем PassengerId
data = pandas.read_csv('train.csv', index_col="PassengerId")


# TODO #1
def get_sex_distrib(data):
    """
    1. Какое количество мужчин и женщин ехало на параходе? Приведите два числа через пробел.
    """

    n_male, n_female = 0, 0
    n_male, n_female = data['Sex'].value_counts()
    return n_male, n_female


# get_sex_distrib(data)

# TODO #2
def get_port_distrib(data):
    """
    2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.
    """

    port_S, port_C, port_Q = 0, 0, 0
    port_S, port_C, port_Q = data['Embarked'].value_counts()
    print(port_S, port_C, port_Q)
    return port_S, port_C, port_Q


# get_port_distrib(data)

# TODO #3
def get_surv_percent(data):
    """
    3. Посчитайте долю погибших на параходе (число и процент)?
    """

    n_died, perc_died = 0, 0
    died, n_died = data['Survived'].value_counts()
    perc_died = died / (died + n_died)
    return n_died, perc_died


# get_surv_percent(data)

# TODO #4
def get_class_distrib(data):
    """
    4. Какие доли составляли пассажиры первого, второго, третьего класса?
    """
    n_pas_f_cl, n_pas_s_cl, n_pas_t_cl = 0, 0, 0
    n_pas_f_cl, n_pas_s_cl, n_pas_t_cl = data['Pclass'].value_counts()
    return n_pas_f_cl, n_pas_s_cl, n_pas_t_cl


# print(get_class_distrib(data))

# TODO #5
def find_corr_sibsp_parch(data):
    """
    5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).
    """

    corr_val = -1
    corr_val = data['SibSp'].corr(data['Parch'], method='pearson')  # return float
    # corr_val = data[['SibSp','Parch']].corr() # return correlation matrix
    return corr_val


# print(find_corr_sibsp_parch(data))

# TODO #6-1
def find_corr_age_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:

    - возрастом и параметром survival;

    """

    corr_val = -1
    corr_val = data['Age'].corr(data['Survived'], method='pearson')
    return corr_val


# print(find_corr_age_survival(data))

# TODO #6-2
def find_corr_sex_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:

    - полом человека и параметром survival;
    """

    corr_val = -1
    level_map = {'male': 0, 'female': 1}  # keys - old, values - new
    data['Sex_map'] = data['Sex'].map(level_map)
    corr_val = data['Sex_map'].corr(data['Survived'], method='pearson')
    return corr_val


# print(find_corr_sex_survival(data))

# TODO #6-3
def find_corr_class_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:

    - классом, в котором пассажир ехал, и параметром survival.
    """

    corr_val = -1
    corr_val = data['Pclass'].corr(data['Survived'], method='pearson')
    return corr_val


# print(find_corr_class_survival(data))

# TODO #7
def find_pass_mean_median(data):
    """
    7. Посчитайте средний возраст пассажиров и медиану.
    """

    mean_age, median = None, None
    mean_age, median = data['Age'].mean(), data['Age'].median()
    return mean_age, median


# print(find_pass_mean_median(data))

# TODO #8
def find_ticket_mean_median(data):
    """
    8. Посчитайте среднюю цену за билет и медиану.
    """

    mean_price, median = None, None
    mean_price, median = data['Fare'].mean(), data['Fare'].median()
    return mean_price, median


# print(find_ticket_mean_median(data))

def parse_name(name_list):
    first_name_list = []
    for i in name_list:
        if '(' in i:
            fn = i.split('(')[1].split(')')[0].split(' ')
        else:
            fn = i.split(". ")[1].split(" (")[0].split(' ')
        for name in fn:
            first_name_list += [name]
    return first_name_list


# TODO #9
def find_popular_name(data):
    """
    9. Какое самое популярное мужское имя на корабле?
    """
    name = ""
    data_with_names = data[['Sex', 'Name']].loc[data['Sex'] == 'male']

    # list of names from series
    name_list = data_with_names['Name'].to_list()
    series_names = pandas.Series(parse_name(name_list))

    name = series_names.value_counts().keys()[0]
    return name


# print(find_popular_name(data))

# TODO #10
def find_popular_adult_names(data):
    """
    10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?
    """
    popular_male_name, popular_female_name = "", ""
    data_with_names = data[['Sex', 'Name', 'Age']].loc[data['Age'] > 15]

    data_with_names_male = data_with_names['Name'].loc[data_with_names['Sex'] == 'male']
    data_with_names_female = data_with_names['Name'].loc[data_with_names['Sex'] == 'female']

    # list of names from series
    name_list_male = data_with_names_male.to_list()
    series_names_male = pandas.Series(parse_name(name_list_male))
    popular_male_name = series_names_male.value_counts().keys()[0]

    name_list_female = data_with_names_female.to_list()
    series_names_female = pandas.Series(parse_name(name_list_female))
    popular_female_name = series_names_female.value_counts().keys()[0]

    return popular_male_name, popular_female_name


print(find_popular_adult_names(data))


# ------------------------------


# Реализуем вычисление количества пассажиров на параходе и опишем предварительные действия с данными (считывание)

# После загрузки данных с помощью метода read_csv и индексации его по первому столбцу данных (PassangerId) становится доступно выборка данных по индексу.
# С помощью запроса ниже мы можем получить имя сотого пассажира
# print((data.iloc[100]['Name']))


def get_number_of_pass(data_file):
    """
        Подсчет количества пассажиров.
        data_file - str
        В качестве аргумента удобнее всего использовать строковую переменную, куда будет передаваться название файла (т. к. далее, возможно, потребуется подсчитать параметры для другого набора данных test.csv)
    """
    male_int, female_int = 0, 0
    # считывание и обработка данных
    data = pandas.read_csv(data_file, index_col="PassengerId")

    # считать данных из столбца возможно с помощью метода value_counts()
    res = data['Sex'].value_counts()
    # res будет содержать ассоциативный массив, ключами в котором являются значения столбца sex, а целочисленные значениями - количества пассажиров обоих полов
    male_int, female_int = res['male'], res['female']
    return male_int, female_int


def test_get_number_of_pass():
    assert get_number_of_pass('train.csv') == (577, 314), " Количество мужчин и женщин на Титанике"
