# take a word
word = input("Enter a word: ")
total = 0

# check to see the number of vowels
for i in range(len(word)):
    if word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u":
        total += 1
# output the number of vowels
print("The word " + word + "has " + str(total) + " vowels")
