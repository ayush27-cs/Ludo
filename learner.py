def add(a,b):return a+b
def subtract(a,b): return a-b
def multiply(a,b):return a*b
def divide(a,b):return a/b
def power(a,b):   return a**b    
def modulus(a,b):return a%b
def floor_division(a,b): return a//b
while True:
    print("Select operation.")
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /, **, %, //) or ayush to abort: ")

    if operation == 'ayush':
        print("Calculator aborted.")
        break
    elif operation == '+':
        print(f"Result: {add(a,b)}")
    elif operation == '-':
        print(f"Result: {subtract(a,b)}")
    elif operation == '*':
     print(f"Result: {multiply(a,b)}")
    elif operation == '/':
     print(f"Result: {divide(a,b)}")
    elif operation == '**':
        print(f"Result: {power(a,b)}")
    elif operation == '%':
        print(f"Result: {modulus(a,b)}")
    elif operation == '//':
        print(f"Result: {floor_division(a,b)}")
    else:
        print("Invalid operation.")


import math
def square_root(a): return math.sqrt(a)
def logarithm(a): return math.log(a)
def sine(a): return math.sin(a)
def cosine(a): return math.cos(a)
def tangent(a): return math.tan(a)
def factorial(a):return math.factorial(a)    
def exponential(a):return math.exp(a)
def radian(a):return math.radians(a)      
def degree(a): return math.degrees(a)  
def cotangent(a): return 1/math.tan(a)    
def secant(a): return 1/math.cos(a)
def cosecant(a): return 1/math.sin(a)
while True:
    print("Select operation.")
    a=int(input("Enter number: "))
    operation = input("Enter operation (sqrt, log, sin, cos, tan, cot, sec, csc, rad, deg) or ayush to abort: ")
    if operation == 'ayush':
        print("Calculator aborted.")
        break
    elif operation == 'sqrt':
        print(f"Result: {square_root(a)}")
    elif operation == 'log':
        print(f"Result: {logarithm(a)}")
    elif operation == 'sin':
     print(f"Result: {sine(a)}")
    elif operation == 'cos':
     print(f"Result: {cosine(a)}")
    elif operation == 'tan':
        print(f"Result: {tangent(a)}")
    elif operation == 'cot':
        print(f"Result: {cotangent(a)}")
    elif operation == 'sec':
        print(f"Result: {secant(a)}")
    elif operation == 'csc':
        print(f"Result: {cosecant(a)}")
    elif operation == 'rad':
        print(f"Result: {radian(a)}")
    elif operation == 'deg':
        print(f"Result: {degree(a)}")
    else:
        print("Invalid operation.")


    #end of code..created a simple calculator
