def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        print("You can't divide by zero")

if __name__ == "__main__":
    print("Adding:", add_numbers(2,4))
    print("Subtracting:", subtract_numbers(9,2))
    print("Multiplying:",  multiply_numbers(3,5))
    print("Dividing:", divide_numbers(8,2))
