n=int(input("Enter the number of terms needed in Fibonacci Series:\n"))
fib=[]
a,b=0,1
for i in range(n):
    fib.append(a)
    a,b=b,a+b
print("The required Fibonacci series is:-\n",fib)
