print("===== UNIVERSITY ADMISSION SYSTEM =====")

# Get student details 

name = input("Enter your name : ")
age = int(input("Enter Your age : "))

english = input("O/L English Result (Pass/Fail): ").lower()
maths = input("O/L Maths Result (Pass/Fail): ").lower()


stream = input ("Enter A/L Stream : ").lower()
average = float(input("Enter A/L Average: "))

print("\n===== ADMISSION REPORT =====")

# validate student name 

if name == "":
    print("Invalid Student Name ")

# validate age 

elif age == "":
    print("Invalid Age ")

elif age < 16 or age > 35 :
    print("Not Eligible : Age Requirment ")

# Validate O/L results

elif(english != "pass" and english != "fail") or \
    (maths != "Pass" and maths!= "fail") :
    print("Invalid O/L Results")

elif english == "fail" or maths == "fail":
    print("Admission Rejected: O/L Requirements")

# Validate A/L stream

elif stream not in ["science,"  "commarce" , "arts" "technology"]:
    print("Invalid A/L Stream")

# Validate A/L average
elif average < 0 or average > 100 :
    print("Invalid Avarage marks ")

else:
    print("Student Name :",name)
    print("Age : " , age)
    print("A/L Stream: ", stream)


# Admission decision

if average >= 75:
    print("Admission Status: Direct Admission")
elif average >= 65 :
    print("Admission Status: Admission Approved")
elif average >= 50 : 
    print("Admission Status: Condition Approved")
else:
    ("Admission Status: Admission Rejected")

# Scholarship decision
if average >= 90 :
    print("Scholarship: 100%")
elif average >= 80:
    print("Scholarship: 50%")
elif average >= 75:
    print("Scholarship: 25%")
else:
    print("Scholarship: No Scholarship")
print("\n Thank you for applying !")