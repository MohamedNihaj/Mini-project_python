marks =  float (input("Enter your marks : "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 75 :
    print("A")
elif marks >= 65 :
    print("B")
elif marks >= 50 :
    print("C")
elif marks >= 35 :
    print ("S")
else:
    print("F")