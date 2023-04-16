# Name-Lastname : Thanapoom Phatthanaphan
# Class : CS 515-D
# Project 1

"""
Question:
An employee’s total weekly pay equals the hourly wage multiplied by
the total number of regular hours plus any overtime pay. Overtime pay
equals the total overtime hours multiplied by 1.5 times the hourly wage.
Write a program that takes as inputs the hourly wage, total regular hours,
and total overtime hours and displays an employee’s total weekly pay.

1. Variables
    hourlyWage = The total wage of working per hour.
    totalRegularHours = The total regular hours of working per week.
    totalOvertimeHours = The total overtime hours of working per week.
    totalWeeklyPay = The total weekly pay for employee.
2. Inputs
    hourlyWage
    totalRegularHours
    TotalOvertimeHours
3. Output
    totalWeeklyPay
4. Computation
    totalWeeklyPay = (hourlyWage * totalRegularHours)
                     + (1.5 * hourlyWage * totalOvertimeHours)
5. Execution step of the program
    Step 1: Input the amount of the hourly wage.
    Step 2: Input the total of regular hours of working.
    Step 3: Input the total overtime hours of working.
    Step 4: The program calculate the total weekly pay for employee
            from those inputs
"""
hourlyWage = float(input("Enter the hourly income ($): "))
totalRegularHours = float(input("Enter the total of regular work hours per week: "))
totalOvertimeHours = float(input("Enter the total of overtime work hours per week: "))
totalWeeklyPay = round((hourlyWage * totalRegularHours)
                       + (1.5 * hourlyWage * totalOvertimeHours), 2)
print("An employee's total weekly pay is {0} dollars".format(totalWeeklyPay))
