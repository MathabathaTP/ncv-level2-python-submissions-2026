secret_number = 12
attempts = 0
guessed_correctly = False

while attempts < 5 and guessed_correctly == False:
    guess = input('Guese a number')
    if guess.isdigit():
        guess_val = int(guess)
        if guess_val < 1 and guess_val > 20:
            print('The correct range is 1 to 20')
        else:
            attempts += 1
            if guess_val == secret_number:
                print('Hao, CORRECT!')
                guess_correctly =True
            elif guess_val < secret_number:
                print('too low')
            else:
                print('too High')

if guessed_correctly ==False:
    print(f'Failed to guess. secred number is  :{secret_number}')