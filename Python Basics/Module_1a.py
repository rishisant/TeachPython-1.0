# Module 1a

import time
import os

print("What's your name?")
name = input("Name: ")

print("Welcome to Teach Python,",name,"!")
print("In this exercise, you will learn about Python basics. This includes variables, if-then statements, and syntax.")
time.sleep(8)
print()

print("You will be using console input in order to learn how to code! Then, after coding, you will perform the exercise associated with your module. In the case of Module 1a, you will code on Exercise 1a.")
time.sleep(5)
print()

print("First off, let's take a little quiz, shall we?")

correctanswers = 5
# Defining the correct answers

print()
time.sleep(7)
os.system('clear')

print("Is 1.5 a floating point value or an integer? Type a for floating point and b for integer. ")
print()
q1 = input("Input answer here: ")
if q1 == "a":
	print("Correct! Good job. Any number with a decimal place is considered a float.")
elif q1 == "b":
	print("Wrong answer! An integer is a whole number value that can be negative or positive.")
	correctanswers -= 1
else:
	print("This input could not be parsed! The question has been marked as incorrect.")
	correctanswers -= 1
	

time.sleep(5)
os.system('clear')

q2 = input("What symbol do you use to mark a comment? Type the symbol. ")
if q2 == "#":
	print("Correct! Good job. A comment is marked with a hashtag or pound symbol.")
else:
	print("This input could not be parsed! The question has been marked as incorrect. The correct answer is #.")
	correctanswers -= 1

time.sleep(5)
os.system('clear')

print("Choose from a, b, or c for the following question.")
print()
print("Which one of the following is a valid variable name?")
print()
print("a) 4_question")
print("b) electric eel_quantity")
print("c) child_age")
q3 = input("Input answer here: ")
if q3 == "c":
	print("Correct! Variables cannot start with numbers or contain spaces within themselves.")
else:
	print("The correct answer is c. Variables cannot contain illegal characters, spaces, and cannot start with numbers.")
	correctanswers -= 1

time.sleep(5)
os.system('clear')

print("This question will involve you typing directly into the console.")
time.sleep(1.5)
print("Create a variable named 'var1' and set it equal to 5.")
q4 = input()
if q4 == "var1 = 5":
	print("Great job. This is correct syntax, and is brilliantly spaced.")
elif q4 == "var1=5":
	print("This is correct, however, it should be spaced better.")
elif q4 == "var1 =5":
	print("This is spaced decently, but I would recommend including a space after the equal sign.")
else:
	print("Your input was not correct! The correct input is as follows.")
	time.sleep(0.5)
	print("var1 = 5")
	correctanswers -= 1

time.sleep(5)
os.system('clear')

print("This question will involve you typing directly into the console.")
time.sleep(1.85)
print("Create a variable named 'age' and set it equal to 10. Space well, or the answer will be counted incorrect!")
q5_a = input()
if q5_a == "age = 10":
	print("Now, add the number 2 to the variable, while changing the variable directly. Space well, or the answer will be counted incorrect!")
	q5_b = input()
	if q5_b == "age += 2":
		print()
		print("Perfect! You have successfully completed Module_1a.")
	else:
		print("The correct answer is as follows:")
		print("age += 2")
		correctanswers -= 0.5
		print()
		print("You have successfully completed Module_1a.")
else:
		print("The correct answer is as follows.")
		time.sleep(0.5)
		print("age = 10")
		print()
		print("You have successfully completed Module_1a.")

print()
print("Your score is being calculated.")
percentage = (correctanswers / 5)*100
percentage = round(percentage,2)
time.sleep(5)
print(name, "scored", percentage, "% on Module_1a!")
time.sleep(2)
print()

if percentage == 100:
	print("You achieved a perfect score! You seem to know your Python basics! Well done!")
elif percentage >= 80:
	print("You barely missed a perfect score! Not too bad,",name,"!")
elif percentage <= 50:
	print("You should look over your notes and learn a bit more about Python basics! Better luck next time,", name, "!")

time.sleep(10)
print()
print("This module has been completed.")
print("If you would like, work on Exercise_1a.py in the folder Python Basics!")