operator = input("What calculation would you like to do? (add, sub, mult, div)")
num1 = int(input("What is number 1?"))
num2 = int(input("What is number 2?"))

result = ""

if operator == "add":
  result = num1 + num2
elif operator == "sub":
  result = num1 - num2
elif operator == "mult":
  result = num1 * num2
elif operator == "div":
  result = num1 // num2

print("Your result is", result, "Calc U Later!")
