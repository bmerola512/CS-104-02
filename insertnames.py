guess = str(input())
ListOfNames = []
namecount = 0
Name = input('-->')
tf = True

while namecount < 10:

    ListOfNames.append(Name)
    print(ListOfNames)
    Name = input('-->')
    namecount += 1

ListOfNames = sorted(ListOfNames)
print(ListOfNames)

print("Enter a name to search for or 'End' to end the program: ")

while tf:

    guess = input('-->')

    if guess == "End":

        print("Goodbye")
        break

    elif guess not in ListOfNames:

        print("The name was not found")

    elif guess in ListOfNames:

        print("The name was found")
