import random

attempts = 0
theComputerNumber = random.randint(1, 1000000)
print(theComputerNumber)
lowGuessRange = 1
highGuessRange = 1000000
gameOver = False
#guess = int(input('Enter a Guess: '))

while gameOver == False:
    guess = int(input("Enter a guess:"))

    if guess <= lowGuessRange or guess >= highGuessRange:
        print("Your guess is out of the range!")
        print("Here's a new range:", lowGuessRange, "and ", highGuessRange)

    elif guess < theComputerNumber:
        lowGuessRange = guess
        attempts += 1
        print("Number is higher than",  lowGuessRange)
        print("Your guess range is",  lowGuessRange, "and ", highGuessRange)

    elif guess > theComputerNumber:
        highGuessRange = guess
        attempts += 1
        print("Number is lower than",  highGuessRange)
        print("range is between",  lowGuessRange, "and ", highGuessRange)

    elif attempts == 20:
        print("Sorry, you've used all 20 attempts.")
        print("The number was: ", theComputerNumber)
        gameOver = True

    elif guess == theComputerNumber:
        attempts += 1
        gameOver = True
        print("You got the number correct! The number was ", theComputerNumber)
        print("You got it in ", attempts, "tries.")
        break






