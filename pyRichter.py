# Python Richter Scale Calculation
# Your first and last name: Brandon Merola
# Your ID: s1267812

# Algorithm:
# ask the user to 'Enter the Richter scale value: '
#   hint1: use an 'input' statement to input a variable called 'richter'
#   hint2: make sure 'richter' is a 'floating point' by using 'float'
# determine the Effect for the Richter scale value entered
#   hint1: use 'if' 'elif' and 'else' statements
#   hint2: remember to use ':' following all 'if' 'elif' and 'else' statements
#  display or print the Effect
#   hint: use 'print' statement (only 1 effect should print)

# test your program several times with the following values:
#   8.1, 8.0, 7.1, 7.0, 6.1, 6.0, 4.6, 4.5, 4,4, -4.6

using = True

while using:

    richter = float(input('Enter the Richter Scale value, or enter 99 to end: '))

    if richter <= 0:
        print('Enter a number greater than 0')
    elif richter == 99:
        using = False
    elif richter >= 8.0:
        print("Most structures fall")
    elif richter >= 7.0:
        print('Many buildings destroyed')
    elif richter >= 6.0:
        print('Many buildings considerably damaged, some collapse')
    elif richter >= 4.5:
        print('damage to poorly constructed buildings')
    else:
        print('No destruction of buildings')


