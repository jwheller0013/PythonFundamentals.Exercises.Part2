def exponentiate (x,y):
	return x**y

def raise_to_fourth_power (z):
	return z**4

square = lambda a: exponentiate(a,2)

cube = lambda b: exponentiate(b,3)

print (square(2)) 

print (cube(2))

print (raise_to_fourth_power(2))
