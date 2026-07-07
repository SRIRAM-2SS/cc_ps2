def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b

print multiply(5, 3)

print divide(12,3)  # Output: 15