# Testing (Not just your own code) & Debugging (Mostly your own code)

Overview

* Why is testing important
* What are the different types of testing
* How do we test
* Aside: Python: Reading input from the user (or another program)

## Aside: Python scripts
* Made similar to the bash script we wrote yesterday
* typically 
* File containing python code (instead of bash command)
* Can be run two different ways
  ** python <my_script.py>
*OR*
  ** replace `#!/bin/bash` with `#!/usr/bin/python`
  ** mark as executable with `chmod +x` command
  ** run from the shell via ./my_script.py

Exercise: hello world script

make a script file named hello.py that prints "Hello world" and run it

## Why do we test?

Short answer? it is easy to make mistakes

## Types of testing

* Unit Testing
* Regression Testing
* System testing*

### System testing
Core idea: Treat the 'system' as a black box.  Feed the system a small set of selected data and compare the system's output to the expected.

* The system could be a biological system
* Hardware system
* Software system
  ** As simple as a program
  ** As complex as a large analysis pipeline

This is what we'll focus on!

Our testing system will be a bug ridden divide function.

## How do we test?

Or, how do we select small sets of data to test with?

Domain knowledge
* I know these types of inputs are common
* I know these types of input are important
* I know these types of inputs could cause problems

EXERCISE: Given that we're working with the divide operation, what are some inputs that could cause problems?

Edit testing_example.py to test possible problematic inputs.

EXERCISE:

* Create a python script named `mean.py`
* Write a function `compute_mean` that computes the mean of a list of numbers
* Come up with several test cases for your function
  ** How does it behave with lists of only integers?
  ** How does it behave with an empty list?

Review of functions

```python
def print_string(s):
    print s
```

Where s is an input parameter

and we can return values from a function as well
```python
def return_2(v):
    return 2

print "Calling return_2(1):", return_2(1)
```

