def fib(n): #this is function for generating fibo series
    if(n==0 or n==1):
        return n
   
    else:
        return fib(n-1) + fib(n-2)
    
# print(fib(5))    
for i in range(10):
 print(fib(i) , end = " , ")