n = input('Please think of a number between 0 and 100! ')

numGuesses = 0

low = 0
high = 100
ans = (high + low) // 2

while ans != n:
    print("Is your secret number " + str(ans) + "?")
    user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
    if user_input not in 'lch':
        print("Sorry, I did not understand your input.")
    else:
        if user_input == 'h':
            high = (high + low) // 2
        elif user_input == 'c':
            break
        else:
            low = (high + low) // 2
        ans = (high + low) // 2

print("Game over. Your secret number was: " + str(ans))