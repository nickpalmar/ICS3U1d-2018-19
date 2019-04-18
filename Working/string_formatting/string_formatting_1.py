# print("Change Counter")
# print("")
# print("Please enter the count of each coin type.")
# quarters = int(input("Quarters: "))
# dimes = int(input("Dimes: "))
# nickels = int(input("Nickels: "))
# pennies = int(input("Pennies: "))
# total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01
# print("")
# print("The total value of your change is ${0:0.2f}".format(total))

# print("Hello {0} {0}, you may have won ${1}".format("Mr.","Smith",1000))
#
# print("This int,{0:5}, was placed in a field of width 5".format(7))
# print("This int,{0:10}, was placed in a field of width 10".format(7))
# print("This flo,{0:10.5f}, has width 10 and is fixed at 5 decimal places".format(3.1415926))
# print("Compare {0} and {0:0.20f}".format(3.14))
#
# print("left justification: {0:<5}!".format(9))
# print("right justification: {0:>5}".format("Hi!"))
# print("centre justification: *{0:^10}*".format("Hell"))
#
# cost1 = 3.07
# tax1 = cost1 * 0.06
# total1 = cost1 + tax1
#
# print("Cost:  ${0:5.2f}".format(cost1))
# print("Tax:    {0:5.2f}".format(tax1))
# print("------------")
# print("Total: ${0:5.2f}".format(total1))



litres_max = 70
fuel_efficiency = 13.9 #L/100km

#table header
print("{0:>16} {1:>22} {2:>15}".format("Litres Used","Distance Travelled", "Hello column"))

for litres in range(0,litres_max,10):
    distance = (100*litres)/fuel_efficiency
    print("{0:>15}L {01:>20.2f}km {2:>15}".format(litres,distance, "hello"))





