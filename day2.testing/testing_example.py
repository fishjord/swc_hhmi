#!/usr/bin/python

import test_function

# The # indicates that this is a comment
# The simplest type of test is to print out the value and compare it by eye to the expected value
print "Return value of divide(100, 5):", test_function.divide(100, 5)
print "Return value of divide(5, 5):", test_function.divide(5, 5)
print "Return value of divide(1, 2):", test_function.divide(1, 2)
print "Return value of divide(1, .5):", test_function.divide(1, .5)

try:
	#open("doesn'texist")
	print "Return value of divide(10, 0):", test_function.divide(10, 0)
except ZeroDivisionError:
	print "Divide by zero"
except IOError:
	print "IO error"
