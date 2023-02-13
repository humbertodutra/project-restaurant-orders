import csv
from collections import Counter
from os import path


def favorite_meal_func(data, name):
    meals = [meal[1] for meal in data if meal[0] == name]
    favorite_meal = Counter(meals).most_common(1)[0][0]
    return favorite_meal


def how_many_times_func(data, name, meal):
    how_many_times = len(
        [order for order in data if order[0] == name and order[1] == meal])
    return how_many_times


def which_meal_never_ordered(data, name):
    person_meals = [meal[1] for meal in data if meal[0] == name]
    all_meals = set([meal[1] for meal in data])
    meals_never_ordered = all_meals - set(person_meals)
    return meals_never_ordered


def days_that_never_ordered(data, name):
    days = set()
    for order in data:
        if order[0] == name:
            days.add(order[2])

    all_days = set(day[2] for day in data)
    never_ordered_days = all_days - days

    return never_ordered_days


def analyze_log(path_to_file):
    if '.csv' not in path_to_file:
        raise FileNotFoundError(f"Extensão inválida: {path_to_file}")

    if not path.exists(path_to_file):
        raise FileNotFoundError(f'Arquivo inexistente: {path_to_file}')

    with open(path_to_file, 'r') as file:
        orders = list(csv.reader(file))
        favorite_meal = favorite_meal_func(orders, 'maria')
        how_many_times = how_many_times_func(orders, 'arnaldo', 'hamburguer')
        meals_never_ordered = which_meal_never_ordered(orders, 'joao')
        days_never_ordered = days_that_never_ordered(orders, 'joao')
        result = (
            f"{favorite_meal}\n"
            f"{how_many_times}\n"
            f"{meals_never_ordered}\n"
            f"{days_never_ordered}"
        )
        with open("data/mkt_campaign.txt", "w") as file:
            file.write(result)


# path_ = './data/orders_1.csv'
# analyze_log(path_)
