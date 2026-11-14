
def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi


def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal Weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


print("===================================")
print("          BMI CALCULATOR")
print("===================================")

try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    if weight <= 0 or height <= 0:
        print("\nInvalid input! Values must be greater than zero.")

    else:
        bmi = calculate_bmi(weight, height)
        category = get_category(bmi)

        print("\n========== BMI RESULT =============")
        print("Weight       :", weight, "kg")
        print("Height       :", height, "m")
        print("BMI          : {:.2f}".format(bmi))
        print("Category     :", category)
        print("===================================")

except ValueError:
    print("\nInvalid input! Please enter numbers only.")
