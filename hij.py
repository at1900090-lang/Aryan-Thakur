num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operator = input("Enter operation (+, -, *, /): ")

match operator:
    case "+":
        print("Answer =", num1 + num2)

    case "-":
        print("Answer =", num1 - num2)

    case "*":
        print("Answer =", num1 * num2)

    case "/":
        if num2 != 0:
            print("Answer =", num1 / num2)
        else:
            print("Cannot divide by zero")

    case _:
        print("Invalid operation")


