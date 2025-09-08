

def sum_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def subtract_numbers(a, b):
    return a - b

if __name__ == "__main__":
    print("Sum:", sum_numbers(10, 5))
    print("Multiply:", multiply_numbers(10, 5))
    print("Divide:", divide_numbers(10, 5))
    print("Subtract:", subtract_numbers(10, 5))

    
    
