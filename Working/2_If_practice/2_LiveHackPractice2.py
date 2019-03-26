# get the marks and earnings prior to summer
mark = int(input("What was your average at the end of the year: "))
earnings = float(input("How much money did you make before summer: "))

# check to see where you are allowed to go
if mark >= 80 and earnings >= 500:
    print("You can go to Europe")
elif mark >= 80:
    print("You can go to California")
else:
    print("You can't go anywhere")