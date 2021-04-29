#recursion activity Fibonacci first 20

#declaring function with one parameter
def fibonacci(n):
#prohibits parameter from being less than 1
   if n <= 1:
       return n
   else:
#parameter given is equal to sum of two previous numbers
#Fibonacci calculation
       return(fibonacci(n-1) + fibonacci(n-2))


#for loop allowing i to loop function being called in next line
#with range to allow it to loop only 20 times
for i in range(20):
    #calling function with parameter i and not n or 20 because we want all the numbers to show
    #because we want all the numbers to show
    print((fibonacci(i)), end = "  ")