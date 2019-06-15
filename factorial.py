def factorial_iterative(n):
    fact = 1
    for i in range(n):
        fact *= (i+1)
    return fact

def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n * factorial_recursive(n-1)
num = int(input("Enter number for factorial"))
print("Factorial using iterative is " + str(factorial_iterative(num)))
print("Factorial using recursive is " + str(factorial_recursive(num)))