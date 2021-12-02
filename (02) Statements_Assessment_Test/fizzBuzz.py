from random import randint
x = randint(1, 100)
text = ''

if x % 3 == 0:
    text += 'Fizz'
if x % 5 == 0:
    text += 'Buzz'

if len(text) == 0:
    print(x)
else:
    print(text)
