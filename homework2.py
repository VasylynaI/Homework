# Exercise 1
# Сформуйте стрінг, в якому міститься інформація про певне слово.
# "Word [тут слово] has [тут довжина слова, отримайте з самого сдлва] letters", наприклад "Word 'Python' has 6 letters".
# Для отримання слова для аналізу скористайтеся константою або функцією input().
my_word = input('Enter some word here: ')

print(f'Word {my_word} has {len(my_word)} letters')

# Exercise 2
# Напишіть программу "Касир в кінотеватрі", яка попросіть користувача ввести свсвій вік (можно використати константу
# або функцію input(), на екран має бути виведено лише одне повідомлення, також подумайте над варіантами,
# коли введені невірні дані).
result = input('Hello! How old are you? ')

try:
    int_result = int(result)
    if int_result <= 0:
        print('You have a strange age!')
    elif int_result <= 7:
        print('Where are your parents?')
    elif int_result <= 16:
        print('This is a movie for adults!')
    elif int_result >= 65:
        print('Show your pension certificate!')
    elif '7' in result:
        print('You will be lucky today!')
    else:
        print('There are no more tickets!')
except:
    print('Please enter the integer')
