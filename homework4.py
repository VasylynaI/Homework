# Exercise 1
# Є list довільних чисел, наприклад [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44].
# Напишіть код, який видалить (не створить новий, а саме видалить!) з нього всі числа,
# які менше 21 і більше 74.

list_1 = [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44]

idx = [n for n, x in enumerate(list_1) if x < 21 or x > 74]
for i in reversed(idx):
    list_1.pop(i)

print(list_1)

# Exercise 2
# Є два довільних числа які відповідають за мінімальну і максимальну ціну.
# Є Dict з назвами магазинів і цінами:{ "cito": 47.999, "BB_studio" 42.999,
# "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166,
# "the_partner": 38.988, "store": 37.720, "roze-tka": 38.003}.
# Напишіть код, який знайде і виведе на екран назви магазинів,
# ціни яких потрапляють в діапазон між мінімальною і максимальною ціною.

lower_limit = 35.9
upper_limit = 37.339

shops = {
    "cito": 47.999,
    "BB_studio": 42.999,
    "momo": 49.999,
    "main-service": 37.245,
    "buy.now": 38.324,
    "x-store": 37.166,
    "the_partner": 38.988,
    "store": 37.720,
    "roze-tka": 38.003}

for key, value in shops.items():
    if value < lower_limit or value < upper_limit:
        print(key)








