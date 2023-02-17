# Exercise 1
# Напишіть функцію, яка визначає сезон за датою. Функція отримує стрінг у форматі "[день].[місяць]"
# (наприклад "12.01", "30.08", "1.11" і тд) і повинна повернути стрінг з відповідним сезоном,
# до якого відноситься ця дата ("літо", "осінь", "зима", "весна")
"""importing the datetime module"""
from datetime import datetime

"""Lists of seasons by month"""
winter = ['12', '01', '02']
spring = ['03', '04', '05']
summer = ['06', '07', '08']
autumn = ['09', '10', '11']

"""Get, format, and validate a date from the user """
def get_date():
    input_date = input("Pleas input your date in format DD.MM? ")
    try:
        formatted_date = datetime.strptime(input_date, '%d.%m').date()
        formatted_date = str(formatted_date)
        list_date = formatted_date.split('-')
        return list_date[1]

    except ValueError:
        print('Invalid date!')

"""Determine the season by the month"""
def found_season(season):
    if season in winter:
        print("It's winter")
    elif season in spring:
        print("It's spring")
    elif season in summer:
        print("It's summer")
    elif season in autumn:
        print("autumn")


current_season = get_date()
found_season(current_season)

# Exercise 2
# Напишіть функцію "Тупий калькулятор", яка приймає два числових аргументи і строковий,
# який відповідає за операцію між ними (+ - / *). Функція повинна повертати значення відповідної операції
# (додавання, віднімання, ділення, множення), інші операції не допускаються. Якщо функція оримала невірний
# тип данних для операції (не числа) або неприпустимий (невідомий) тип операції вона повинна повернути None
# і вивести повідомлення "Невірний тип даних" або "Операція не підтримується" відповідно.

"""The function accepts two numeric arguments and a string, which is responsible 
for the operation between them (+ - / *)."""
def foo(operator1, operator2, symbol):
    try:
        return eval(str(operator1) + symbol + str(operator2))
    except:
        print('Invalid data type')
        return None



