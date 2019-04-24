print("**** Ounces to Grams Converter ****")
print("This program will print out a titled table that can be used to convert ounces to grams, ")
print("for values from 1 to 15 ounces (1 ounce = 28.35 grams)")

# output the header with formatting
print("{0:>10} {1:>10}".format("Ounces", "Grams"))

grams = 28.35
# loop through the values to create a table
for i in range(1, 16):
    print("{0:>10} {1:>10.2f}".format(i, grams*i))


