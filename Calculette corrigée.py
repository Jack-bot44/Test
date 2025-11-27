while True:
    num1 = float(input("Enter first number: "))
    operateur = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    if operateur == "+":
        print(num1 + num2)
    elif operateur == "-":
        print(num1 - num2)
    elif operateur == "*":
        print(num1 * num2)
    elif operateur == "/":
        print(num1 / num2)
    else:
        print("Invalid operator :(")
    Decision = input("Do you want to continue ?")
    if Decision.lower () != "yes":
        exit()
