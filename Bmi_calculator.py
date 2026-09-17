def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)
    return bmi


def check_bmi(bmi):
    if bmi < 16:
        return "Severe Thinness"
    elif bmi < 17:
        return "Moderate Thinness"
    elif bmi < 18.5:
        return "Mild Thinness"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    elif bmi < 35:
        return "Obese Class I"
    elif bmi < 40:
        return "Obese Class II"
    else:
        return "Obese Class III"


user = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = bmi_calculator(weight, height)
category = check_bmi(bmi)

print("Your BMI is:", round(bmi, 2))
print("Category is:", category)

        