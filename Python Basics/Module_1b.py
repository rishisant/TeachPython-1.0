# Module 1a

import time
import os

print("What's your name?")
name = input("Name: ")

print("Welcome to Teach Python,",name,"!")
print("In this exercise, you will learn about Python basics. This includes variables, if-then statements, and syntax.")
time.sleep(8)
print()

print("You will be using console input in order to learn how to code! Then, after coding, you will perform the exercise associated with your module. In the case of Module 1b, you will code on Exercise 1b.")

time.sleep(5)
print()
print('If you recall, in Exercise_1a you created your own calculator with basic input commands. You also stored variables, and so on.')
time.sleep(1.5)
print('If you have not completed Exercise_1a, I highly encourage you to do so.')
time.sleep(1.5)
print()
print('We will be taking a post-exercise quiz over Exercise_1a.')
time.sleep(5)
print()
print("Let's begin!")
time.sleep(5)

score = 8
os.system('clear')

print('In Exercise_1a, you learned how to create user inputs.')
time.sleep(1.5)
print("Create a variable named 'inp1' and set it equal to an input with no string value (nothing inside the input, so a blank input) and use proper spacing! You will be given no credit if the spacing is not right.")
q1 = input()
if q1 == "inp1 = input()":
	print("Good job! You used perfect spacing and demonstrated your knowledge of inputs quite well!")
else:
	print("You did not type the answer correctly. The desired input is as follows:")
	print()
	print("inp1 = input()")
	score -= 1

time.sleep(5)
os.system('clear')
print('What is elif short for?')
print('a) else')
print('b) enter if')
print('c) else if')
q2 = input()
q2 = q2.lower()
if q2 == 'a':
	print('Close, but not quite. Half a point is deducted off, because you forgot one more word, and that is if! Good try!')
	score -= 0.5
if q2 == 'b':
	print('Not quite. The correct answer was c) else if.')
	score -= 1
if q2 == 'c':
	print('Correct! elif is short for else if.')

time.sleep(5)
os.system('clear')
print('The next question will be worth multiple points. You will code a program in the console, according to the instructions. It is important to use proper spacing, otherwise points may be deducted.')
time.sleep(3)
print()
print("Create a variable named 'num1' and set it equal to the string '15'.")
print()
print('Hint: 15 is a string value!')
q3 = input()
if q3 == "num1 = '15'":
	print('Good answer! That was one of the ways you could mark 15 as a string.')
elif q3 == "num1 = str('15')":
	print('Good answer! That was one of the ways you could mark 15 as a string.')
elif q3 == "num1 = string('15')":
	print('Good answer! That was one of the ways you could mark 15 as a string.')
elif q3 == 'num1 = str("15")':
	print('Good answer! That was one of the ways you could mark 15 as a string.')
elif q3 == 'num1 = string("15")':
	print('Good answer! That was one of the ways you could mark 15 as a string.')
else:
	print('You might have mistyped or misspaced your answer! We will be moving on to the next part.')
	print()
	print('A possible desired answer is as follows:')
	print("num1 = str('15')")
	score -= 2.25

time.sleep(5)
os.system('clear')
print('Next question:')
print('Convert the string value of num1 to a floating point value! Write the code in order to do so, and use proper spacing.')
q4 = input()
if q4 == "num1 = float(num1)":
	print('Correct! You converted the variable num1 to a float variable!')
elif q4 == "float(num1)":
	print("Although you converted the variable into a float,you did not set it equal to 'num1' in order to mark 'num1' as a floating point value.")
	print('Partial credit has been awarded.')
	score -= 1
else:
	print('You did not get the question right. The desired input is as follows:')
	print('num1 = float(num1)')
	score -= 2.5

time.sleep(5)
os.system('clear')
print('Bonus question!')
print("What number was the variable 'func' associated with for multiplication in Exercise_1a?")
q5 = input('Type 1, 2, 3, or 4: ')
if q5 == '3':
	print('Correct! You have been awarded 5 points for your answer!')
	bonus = bool(True)
else:
	print('The correct answer was 3! You did not lose any points, but you did not gain any either!')

print("You have successfully completed Module_1b.")
print()
print("Your score is being calculated.")
percentage = (score / 8)*100
percentage = round(percentage,2)
if bonus == bool(True):
	percentage += 5.00
time.sleep(5)
print(name, "scored", percentage, "% on Module_1a!")
time.sleep(2)
print()

if percentage >= 100:
	print("You achieved a great score! Well done, and keep working hard on your Python basics!")
elif percentage >= 80:
	print("You were just a bit off of a perfect score! Not too bad,",name,"!")
elif percentage <= 50:
	print("You should look over your notes and learn a bit more about Python basics! Better luck next time,", name, "!")

time.sleep(10)
print()
print("This module has been completed.")
print("If you would like, work on Exercise_1b.py in the folder Python Basics!")

