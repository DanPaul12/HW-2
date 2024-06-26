
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
num3 = float(input("Enter your third number: "))

if num1 >= num2 and num1 >= num3:
    print("your largest number is", num1)
if num2 >= num1 and num2 >= num3:
    print("your largest number is", num2)
if num3 >= num1 and num3 >= num2:
    print("your largest number is", num3)


if num1 <= num2 and num1 <= num3:
    print("your smallest number is", num1)
if num2 <= num1 and num2 <= num3:
    print("your smallest number is", num2)
if num3 <= num1 and num3 <= num2:
    print("your smallest number is", num3)