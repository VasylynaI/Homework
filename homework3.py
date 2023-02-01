# Exercise 1
# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є буква "о"
# (враховуються як великі так і маленькі). Цикл не повинен завершитися, якщо користувач ввів слово без букви "о".
while True:
    user_input = input('Enter the word that contains the letter "o": ')
    user_input = user_input.lower()

    if 'o' not in user_input:
        print('Try again!')
        continue

    if user_input:
        print('Great job!')
        break

# Exercise 2
# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2), який містить лише змінні типу стрінг,
# які присутні в lst1. Зауважте, що lst1 не є статичним і може формуватися динамічно від запуску до запуску.

list_1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
new_list = []

for elem in list_1:
    if type(elem) is str:
        new_list.append(elem)

print(list_1)
print(new_list)

# Exercise 3
# Є стрінг з певним текстом (можна скористатися input або константою).
# Напишіть код, який визначить кількість слів в цьому тексті, які закінчуються на "о"
# (враховуються як великі так і маленькі).
my_str = 'you do not have tO go tO the school'
my_str = my_str.lower()
my_list = my_str.split()
result = []

for elem in my_list:
    if elem[-1] == 'o':
        result.append(elem)
print(len(result))
