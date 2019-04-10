# get 3 side lengths from user input
side_one = int(input("Enter the side length of a triangle: "))
side_two = int(input("Enter the side length of a triangle: "))
side_three = int(input("Enter the side length of a triangle: "))

# compute the squre a=values of the sides
sq_1= side_one**2
sq_2 = side_two**2
sq_3 = side_three**2

# check if it is a right triangle or not, and output the result
if (sq_1 + sq_2) == sq_3 or (sq_2 + sq_3) == sq_1 or (sq_1 + sq_3) == sq_2:
    print("This is a right triangle")
else:
    print("This is not a right triangle")