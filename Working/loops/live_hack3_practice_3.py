
print("*** Mark Groups ***")
print("This program takes a collection of marks and counts how many outstanding scores (90-100), satisfactory scores (60-89), and the number of unsatisfactory scores (1-59).")

# set total number of each exam score
outstanding_score = 0
satisfactory_score = 0
unsatisfactory_score = 0

# initialize the loop to run atleast once
go_again = "y"

while go_again == "y":
    # get input from the user(about exam)
    mark = int(input("Enter a mark from 0-100: "))
    while mark < 1 or mark > 100:
        print("Invalid")
        mark = int(input("Enter a mark from 0-100: "))

    # check to see the category of the marks
    if mark >= 1 and mark <= 59:
        unsatisfactory_score += 1
    elif mark <= 89:
        satisfactory_score += 1
    elif mark <= 100:
        outstanding_score += 1
    else:
        print("Invalid mark entered")

    # ask the user if they would like to go again
    go_again = input("Do you wish to enter another mark? (y/n): ")
    while go_again != "y" and go_again != "n":
        print("Invalid")
        go_again = input("Do you wish to enter another mark? (y/n): ")

# output the number of each type of score
print("The number of outstanding marks is", outstanding_score)
print("The number of satisfactory marks is", satisfactory_score)
print("The number of unsatisfactory marks is", unsatisfactory_score)

