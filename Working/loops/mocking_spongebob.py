def mocking_spongebob(sentence):
    meme = ""
    length_sentence = len(sentence)
    position = 0

    while position < length_sentence:
        if sentence[position] == " ":
            meme += " "
            position += 1
        elif position % 2 == 0:
            meme += sentence[position].lower()
            position += 1
        else:
            meme += sentence[position].upper()
            position += 1

    return meme


print(mocking_spongebob("good morning class"))