Exercise: Decorators
Create a decorator function to check that the argument passed to the function factorial is a non-negative integer:

Create a factorial function which finds the factorial of a number.

Use the decorator to decorate the factorial function to only allow factorial of non-negative integers.

example: 

    factorial(1.354) : raise Exception or print error message
    factorial(-1) : raise Exception or print error message
    factorial(5) : 60
