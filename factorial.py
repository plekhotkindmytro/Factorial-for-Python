import sys

def factorial(num):
	fact = 1
	for i in range(0, num):
		fact *= (i+1)
	return fact

if len(sys.argv) == 2:
	numString = sys.argv[1]
	if not(numString.isdigit()):
		print "Entered value is not a positive. Please enter a positive integer."
	else:
		num = int(numString)
		print factorial(num)
else:
	print "Please provide a positive integer argument when invoking the script to get a factorial"
	
