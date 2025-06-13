#Basic Mathematical operation program

#Take two number as input from user

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#perform operations
add = num1 + num2
sub = num1 - num2
mul = num1 * num2

#check foe division by zero
if num2 != 0:
    div = num1 / num2
else:
    div ="undefined(cannot divided by zero)"

    #display the result

    print("\nResult:")
    print(f"Addition: {add}")
    print(f"Subtraction: {sub}")
    print(f"Multiplication: {mul}")
    print(f"Division: {div}")
