from lib import foo
from lib import found_season
from lib import get_date
import time

# Exercise 2
# Візьміть функції з попереднього ДЗ, покладіть їх у файл lib.py і імпортуйте в основний файл для виконання

"""функція, яка визначає сезон за датою. Функція отримує стрінг у форматі "[день].[місяць]"
# (наприклад "12.01", "30.08", "1.11" і тд) і повинна повернути стрінг з відповідним сезоном,
# до якого відноситься ця дата ("літо", "осінь", "зима", "весна")"""

current_season = get_date()
found_season(current_season)

"""The function accepts two numeric arguments and a string, which is responsible 
for the operation between them (+ - / *)."""
print(foo(1, 2, '+'))

# Exercise 1
# Напишіть декоратор, який визначає час виконання функції. Заміряйте час іиконання функцій
# з попереднього ДЗ

def function_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Час виконання функції: {end - start} секунд.")
        return result

    return wrapper

@function_execution_time
def foo(operator1, operator2, symbol):
    try:
        return eval(str(operator1) + symbol + str(operator2))
    except:
        print('Invalid data type')
        return None









