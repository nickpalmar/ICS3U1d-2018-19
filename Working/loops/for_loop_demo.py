#
# def hello5():
#     # output hello 5 times
#
#     for i in range(5):
#         print("hello")
#
#
# hello5()
#
# def count_back():
#     """
#     Countdown from 20 to 1
#     :return: None
#     """
#
#     for i in range(20, 0, -1):
#         print(i)

# count_back()

def km_to_miles():
    # output a table of km to miles conversions from 0 to 100

    for i in range(1, 105, 5):
        if i > 1:
            i -= 1
        miles = i * 0.621

        print(i, "km =", round(miles, 2), "miles")


km_to_miles()



