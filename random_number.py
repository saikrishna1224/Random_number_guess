import random
number = random.randint (1,100)

player_name = input("Hello, What's  your name?")
number_of_guesses = 0
print('Hey ' + player_name + ' Now you want to guess a number between 1 and 100:' )

while number_of_guesses < 8:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print ('your guess is too low')
    if guess > number :
            print('your guess is too high')
    if guess == number :
        break
if guess == number:
         print ('you are guessed correct number in '  +  str (number_of_guesses) + 'tries!')
         print('Thank you for playing , hope u have a great day ahead')
else:
         print('you did not guessed the number in given chances , the number was ' + str (number))
         print('sorry better luck next time mate')