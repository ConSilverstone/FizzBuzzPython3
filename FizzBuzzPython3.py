## A program demonstraiting FizzBuzz ##

## Initilise Variables ##
fizz = 3 # For values that are multiple of this print fizz
buzz = 5 # For values that are multiple of this print buzz

for i in range (100):
    if (i % fizz == 0 and i % buzz != 0): ## For values that are a multiple of fizz BUT NOT buzz
        print ("Fizz")
    elif (i % fizz == 0 and i % buzz != 0): ## For values that are a multiple of buzz BUT NOT fizz
        print ("Buzz")
    elif (i % fizz == 0 and i % buzz == 0): ## For value that are multiple of both!
        print ("FizzBuzz")
    else:
        print(i) ## Otherwise just print number
    i += 1