# Name-Lastname: Thanapoom Phatthanaphan

"""
This is the program to simulate the population growth rate by assuming
that none of the organisms die.

Inputs:
    numberOfOrganisms = the number of organisms
    growthRate = the rate of the population growth (a real number greater than 0).
    cycleHoursGrowth = the number of hours it takes to achieve this rate.
    totalHoursGrowth = the total hours that the population grow.

Operating steps:
    Step 1: Enter the initial number of organisms.
    Step 2: Enter the rate of the population growth.
    Step 3: Enter the number of hours it takes to achieve this rate.
    Step 4: Enter the total hours that the population grow.
    Step 5: The program calculates and display the final number of organisms.
"""

# Enter all inputs.

numberOfOrganisms = int(input("Enter the initial number of organisms: "))
growthRate = float(input("Enter the rate of the population growth: "))
while growthRate < 0:
    growthRate = float(input("Please re-enter the rate of the population growth: "))
cycleHoursGrowth = int(input("Enter the number of hours it takes to achieve this rate: "))
totalHoursGrowth = int(input("Enter the total hours that the population grows: "))

# Calculate the total number of organisms.

for i in range(1, (totalHoursGrowth // cycleHoursGrowth) + 1):
    numberOfOrganisms = numberOfOrganisms * growthRate

# Display the total number of organisms after growth period.

print("The total organisms are {0}".format(numberOfOrganisms))