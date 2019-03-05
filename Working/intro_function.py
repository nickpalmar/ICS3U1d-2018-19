
def happy():
    print("Happy birthday to you")

def sing(person):
    print("Happy birthday to " + person)


def main():
    # global person
    person = input("Enter your name:")
    happy()
    happy()
    sing(person)
    happy()



main()