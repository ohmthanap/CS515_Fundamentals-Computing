"""
This is a program to convert the form of number from octal to decimal.
"""

decNum = int(input("Please enter a decimal integer: "))
octNum = ""
remainder = 0

while decNum > 0:
    remainder = decNum % 8
    decNum = decNum // 8
    octNum = str(remainder) + octNum

print("The octal integer is", octNum)
