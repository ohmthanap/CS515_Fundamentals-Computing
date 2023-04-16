"""
This is a program to convert the form of number from octal to decimal.
"""

octNum = input("Please enter an octal integer: ")
decNum = 0
octPow = len(octNum) - 1
for digit in octNum:
    if digit == '8' or digit == '9':
        print("You input the wrong format of octal number")     # Check the format of an octal number
        decNum = "null"
        break
    else:
        decNum = decNum + int(digit) * (8 ** octPow)      # Computation
        octPow -= 1

print("The decimal integer is", decNum)
