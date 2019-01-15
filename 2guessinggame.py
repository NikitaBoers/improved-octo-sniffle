from random import randint

number = randint(1,10)
print(number)

guess = int(input('Guess my number: '))


while guess != number:
    print('Boo!')
    if guess > number:
        print('Guess Lower')
    elif guess < number:
        print('Guess Higher')
    else:
        print()
    guess = int(input('Guess my number: '))
    
        

print('Yay!')