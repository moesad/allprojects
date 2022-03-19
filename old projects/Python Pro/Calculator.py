#Mohammed Sadiq Project

while True:

        num1 = float(input("please inter first number: "))

        operator = input("please inter operator: ")

        num2 = float(input("please inter second number: "))

        if operator == "+":
            print(num1 + num2)

        elif operator == "-":
            print(num1 - num2) 

        elif operator == "*":
            print(num1 * num2) 

        elif operator == "÷":
            print(num1 // num2) 

        elif operator == "**":
            print(num1 ** num2)

        else:
            print("Wrong entry, please enter valid values")    

        v = input("do yo want to complite?, y, n:  ")   
        if v == 'n':
            break
        