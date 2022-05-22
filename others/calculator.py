from textwrap import dedent

def add(x, y):
    # add x y
    return x + y

def subtract(x, y):
    # subtract x y
    return x - y

def multiply(x, y):
    # multiply x y
    return x * y

def divide(x, y):
    # divide x y
    return x / y


print(dedent("""
    Please select the operation:
    1. add
    2. subtract
    3. multiply
    4. devide"""))
choose = input("(1,2,3,4)> ")
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))


if choose == "1":
    print(f"The number is {add(num1,num2)}")

elif choose == "2":
    print(f"The number is {subtract(num1,num2)}")

elif choose == "3":
    print(f"The number is {multiply(num1,num2)}")

elif choose == "4":
    print(f"The number is {divide(num1,num2)}")