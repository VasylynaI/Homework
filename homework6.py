# Exercise 1
# Напишіть функцію, яка приймає два аргументи.
# Якщо обидва аргумени відносяться до числових типів функція пермножує ці аргументи і
# повертає результат. Якшо обидва аргументи відносяться до типу стрінг функція обʼєднує їх в один і повертає
# В будь-якому іншому випадку - функція повертає кортеж з двох агрументів
def my_function(arg1, arg2):

    if is_int(arg1) and is_int(arg2):
        return arg1 * arg2

    elif is_str(arg1) and is_str(arg2):
        return f'My string: {arg1} {arg2}'

    else:
        return (arg1, arg2)

def is_str(arg):
    return isinstance(arg, str)

def is_int(arg):
    if type(arg) in (float, int):
        return float, int

# Exercise 2
# Напишіть программу "Касир в кінотеватрі", яка попросіть користувача ввести свсвій вік (можно використати константу або функцію input(), на екран має бути виведено лише одне повідомлення, також подумайте над варіантами, коли введені невірні дані).
# якщо користувачу менше 7 - вивести повідомлення"Де твої батьки?"
# якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
# якщо користувачу більше 65 - вивести повідомлення"Покажіть пенсійне посвідчення!"
# якщо вік користувача містить цифру 7 - вивести повідомлення "Вам сьогодні пощастить!"
# у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!"
def take_user_age():
    try:
        user_age = int(input('Hello! How old are you? '))
        return user_age
    except:
        print('Please enter the integer')
        return take_user_age()

def checking_user_age(age):
    if '7' in str(age) or age == 7:
        print('You will be lucky today!')
    elif age <= 7:
        print('Where are your parents?')
    elif age <= 16:
        print('This is a movie for adults!')
    elif age >= 65:
        print('Show your pension certificate!')
    else:
        print('There are no more tickets!')

def validation_user_age():
    while True:
        user_answer = take_user_age()
        if user_answer <= 0 or user_answer > 100:
            print('You have a strange age!')
        else:
            checking_user_age(user_answer)
        break

def game():
    validation_user_age()

game()











