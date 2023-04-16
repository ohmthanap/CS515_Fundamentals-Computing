# Thanapoom Phatthanaphan
# This is the program to sing Happy Birthday song

def happy():
    print("Happy Birthday to you")


def sing(person):
    happy()
    happy()
    print("Happy Birthday, dear " + person)
    happy()

def main():
    name = input("Please enter your name: ")
    sing(name)

main()
