
def moh():
    
    try:
        num1 = float(input ("enter first number:"))

        operator = input ("enter the operator: ") 

        num2 = float(input ("enter first number:"))

        if operator == "+" :
            print (num1 + num2)

        elif operator == "-":
            print (num1 - num2)
            
        elif operator == "/":
            print (num1 / num2)

        elif operator == "*":
            print (num1 * num2)

        else:
            print("wrong write")
    except ValueError as err:
        print(err)    
moh()


print("mohammed")

moh()