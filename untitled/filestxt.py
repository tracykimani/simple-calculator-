import random
print('you are going to play guess game with computer')
print('Rules are as follows')
print('computer guess and you too')
print('if your guess equals computer guess')
print('you wins')
print('maximum guess allowed are 3')
print('we are starting the game ')
print('ready to play with pycharm?')
num = 3
print(num, 'guesses left')
print('guess the number between 1 to 10')
while True:
    guess = input()
    computer = random.randint(1, 10)
    print('you guessed, guess')
    print('computer guesses, computer')
    print()
    if 0<int(guess)<11 and (int(guess) == computer):
        print('YAYY! you wins')
        break
    elif num == 1:
        print('no guesses left\nyou loose the game')
        break
    else:
        print('sorry guess again')
        num = num - 1
    print(num, 'guesses left')
    print('Guess the number between 1 to 10')


