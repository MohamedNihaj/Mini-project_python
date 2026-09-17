#simple calculator

def add(a,b):
    return a + b

def substract(a,b):
    return a - b

def multiply (a,b):
    return a * b 

def divide(a,b):
    if b == 0 :
        return "cannot divide by zero"
    return a / b

print("===Calualtor===")
print("1.addition")
print("2.substract")
print("3.multiply")
print("4.divide")

choose = input("Choose your number (1-4) :")

num1 = float(input("Enter your number : "))
num2 = float(input("Enter your number : "))

if choose == "1":
    result = add(num1,num2)

elif choose == "2":
    result =substract(num1,num2)

elif choose == "3":
    result = multiply(num1,num2)

elif choose == "4":
    result = divide(num1,num2)

else:
    result = "Invalid Number"

print("Results = ",result)