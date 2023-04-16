# Name-Lastname: Thanapoom Phatthanaphan

"""
This is the program to calculate the sum and average of a series of numbers
"""

theSum = 0
count = 0
while True:
    number = input("Please enter a number or press \"Enter\" to quit: ")
    if number <= (0 or ""):
        break
    theSum += float(number)
    count += 1

print("The sum is {0}".format(theSum))
if count == 0:
    print("The average is 0")
else:
    print("The average is {0}".format(float(theSum / count)))