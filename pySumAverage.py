# Sum/Average Program
# Your first and last name: Brandon Merola
# Your student ID: s1267812

# Build on what you did in the 'List of Names' program
# Instead of entering 10 names, enter 20 numbers
# Instead of searching for a name in the list
#   Compute the sum of all 10 numbers
#   Compute the average for all 10 numbers

# Enter a number:
# The sum of the numbers you entered is:
# The average of the numbers you entered is:

from statistics import mean
ListOfNum = []
numcount = 0
num = int(input('Enter a number -->'))
tf = True

while numcount < 20:

    ListOfNum.append(num)
    print(ListOfNum)
    num = int(input('Enter a number -->'))
    numcount += 1

ListOfNum = sorted(ListOfNum)
print(ListOfNum)

# This is where user chooses operator.

print("Enter an operation ('Sum' or 'Average') to perform or type 'End' to end the program: ")

while tf:

    operation = input('-->')

    if operation == "End":

        print("Goodbye")
        break

    elif operation == "Average" or "average":

        print(float(mean(ListOfNum)))

    elif operation == "Sum" or "sum":

        print(float(sum(ListOfNum)))
