def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b

n=50
print ("The Fibonacci of "+ str(n)+" is: " ,end="")
fibonacci(n)