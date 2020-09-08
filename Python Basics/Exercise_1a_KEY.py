# Exercise_1a_KEY
# Do not look at this unless you are stuck on Exercise_1a!

# Today, you will be coding an input calculator! Sounds fun, right? Not really? Eh, anyways, let's get started.

# Start by creating your first line of code.

# From the console, print the following lines.
# 'Welcome to this custom calculator!'
# 'Would you like to add, subtract, multiply, or divide?'

print('Welcome to this custom calculator!')
print('Would you like to add, subtract, multiply, or divide?')

# After printing that line, create your first input variable.

# Let's name it inp1.
inp1 = input('Type + for addition, - for subtraction, * for multiply, and / for divide.')

# We should add the input command, which is input('INSERT STRING')
# Inside the parentheses of an input command is a prompt, which the user will see during the input.

# For example, the following variable will print this line to the console.
# input1 = input('This is an input. Answer here: ')
# This is an input. Answer here: _

# It is important to have a short and sweet variable for your input, since you will call on it quite often. 
# By calling on a variable, you are directly referencing the variable in your code, meaning that you are using its functionalities through a reference.

# Remember that variable 'inp1'? Inside of the input() command, type the following string:

# 'Type + for addition, - for subtraction, * for multiply, and / for divide. '

# Now that you've created 'inp1' with an input value, it's time to reference the variable here!

# We will be working with an if/elif/else statement right now. 'Elif' is short for else if.

# An if statement works as follows. For example, let's say we have a variable x. Let's say if it was equal to 5, we would print the string, 'The number is 5!', but if it was below 5, we would print the string, 'The number is below 5.'

# It would look as follows in the code.
#x = 5 #Input number equal to or below 5 here
# if x = 5:
#	print('The number is 5!')
# elif x < 5:
#	print('The number is below 5.')

# This tells the console to verify if our variable x is equivalent to or below 5, and then send a print command to the console based on the verification.

# Let's go back to our calculator, shall we?
# Let's use an if and three elif statements to verify if the string is equal to '+', '-', '*', or '/'
# Not only that, but let's create another variable, 'func', which is short for function.
# 'func' will serve as our marker that the user has chosen addition, subtraction, multiplication, or division.

# If the user chooses addition, set func to 1, if subtraction, to 2, and for multiplication and division, 3 and 4 respectively.

if inp1 == '+':
	print("You have chosen addition!")
	func = 1
elif inp1 == '-':
	print("You have chosen subtraction!")
	func = 2
elif inp1 == '*':
	func = 3
elif inp1 == '/'
	func = 4

# Once you have finished those lines of code, now we must create two new inputs.

# Create two variables, 'inp2' and 'inp3', and set them equal to a new input command.

inp2 = input('Enter the first number: ')
inp3 = input('Enter the second number: ')

# Once that is done, call on your previous variable, 'func', to determine whether you should add, subtract, multiply, or divide those numbers!

if func = 1:
	print(inp2, "+", inp3, "=", inp+inp3)
elif func = 2:
	print(inp2, "-", inp3, "=", inp2-inp3)
elif func = 3:
	print(inp2, "*", inp3, "=", inp2*inp3)
elif func = 4:
	print(inp2, "/", inp3, "=", inp2/inp3)

print()

# Print a blank line after that, and voila, you have created a calculator! Albeit simple, you have learned how to use if and elif statements in order to parse certain values! Congrats!

# If you are having trouble, check out Exercise_1a_KEY, which has the entire exercise completed for you. You can reference it if you're having trouble.

# Only look at the keys if you are having trouble!