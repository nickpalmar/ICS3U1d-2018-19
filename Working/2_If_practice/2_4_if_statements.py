# squirrel play

def squirrel_play(temp, is_summer):
    if temp >= 60:
        if temp <= 100 and is_summer == True:
            return True
        elif temp <= 90:
            return True
        else:
            return False

    else:
        return False

print(squirrel_play(70, False))
print(squirrel_play(95, False))
print(squirrel_play(95, True))