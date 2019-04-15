def num_string_right(number):
    str_num  = str(number)
    word_number = ""

    for i in range(len(str_num)-1, -1, -1):
        if str_num[i] == "1":
            word_number += "one "
        elif str_num[i] == "2":
            word_number += "two "
        elif str_num[i] == "3":
            word_number += "three "
        elif str_num[i] == "4":
            word_number += "four "
        elif str_num[i] == "5":
            word_number += "five "
        elif str_num[i] == "6":
            word_number += "six "
        elif str_num[i] == "7":
            word_number += "seven "
        elif str_num[i] == "8":
            word_number += "eight "
        elif str_num[i] == "9":
            word_number += "nine "

    return word_number


new_word = num_string_right(32457)
print(new_word)
