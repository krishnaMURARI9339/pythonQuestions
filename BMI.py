# create a BMI calculator in python

def calculate_bmi(weight, height):

    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    return round(bmi, 2), category

def main():
    print("BMI Calculator")
    print("----------------")
    
    weight = float(input("Enter weight (in kg): "))
    height = float(input("Enter height (in meters): "))
    
    bmi, category = calculate_bmi(weight, height)
    
    print(f"\nYour BMI: {bmi}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()
