
# This is exercise 9 from https://github.com/py-study-group/beginner-friendly-programming-exercises/blob/master/exercises.md
#
# Kathryn Marks
# kathryn.pythonprograms@gmail.com
# Created August 8, 2023
# Last modified August 8, 2023

# There are three classes, physics, chemistry and calculus
# Have the user input their grade (1-10) and then average them
# Given the output, print a message given the average >7 "Great job!" 6>average>4 "You need to work harder" and <3 "You Failed"

# The variables are physics, chemistry and calculus

# int((input))) converts the input to a int, otherwise it will be a string

physics = int(input("Please type in your Physics grade and press enter: ")) 
print ("Your Physics grade is: ", physics)

chemistry = int(input("Please type in your Chemistry grade and press enter:  "))
print ("Your Chemistry grade is ", chemistry)

calculus = int(input("Please type in your Calculus grade and press enter:  ")) 
print ("Your Calucus grade is ", calculus)

# Calculate the average grade and print it for the user

total = physics + chemistry + calculus
average = total/3

print ("Your avereage grade is:", average)
