# Exercise 1
my_word = input('Enter some word here: ')

print(f'Word {my_word} has {len(my_word)} letters')

# Exercise 2
result = input('Hello! How old are you? ')
try:
    if int(result) <= 7:
        print('Where are your parents?')
    elif int(result) <= 16:
        print('This is a movie for adults!')
    elif int(result) >= 65:
        print('Show your pension certificate!')
    elif '7' in result:
        print('You will be lucky today!')
    else:
        print('There are no more tickets!')
except:
    print('Please enter the integer')git





