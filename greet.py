def greet(name):
	print("Welcome to my code "+str(name))

def name_input():
	name= input("Please enter your name:\n")
	return name

name=name_input()

greet(name)
