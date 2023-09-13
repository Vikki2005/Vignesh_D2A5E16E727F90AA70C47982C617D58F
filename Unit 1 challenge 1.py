def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Replace '5' with the number for which you want to calculate the factorial
num = 5
result = factorial_recursive(num)
print("Factorial of", num, "is", result)
