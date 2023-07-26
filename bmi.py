
#MEDTECH Iungo DataCamp
#Josephat Hema Submission

#PATIENTS BMI REGISTER:
#PERSONAL INFO

#input

users_first_name = input("Enter your first name: ")
users_second_name = input("Enter your second name: ")
users_age = int(input(f"Hi {users_first_name} {users_second_name}, enter your age: "))
users_gender = input("Enter your gender: ")
users_address = input(f"What is your address, {users_first_name}?: ")
users_phone = input("Enter your mobile number: ")

#Create a dictionary
personal_details = {
    "first name" : users_first_name,
    "second name" : users_second_name,
    "gender" : users_gender,
    "age" : users_age,
    "address" : users_address,
    "mobile number": users_phone
}

#Print Dictonary
print(personal_details)


#BMI

def calculate_bmi(weight, height):
    # weight in kilograms and height in meters.
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    #Interpret the BMI categories
    if bmi < 18:
        return "Underweight"
    elif 18 <= bmi < 24:
        return "Normal weight"
    elif 24 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    # User input for weight and height
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Interpret BMI
    category = interpret_bmi(bmi)

    # Print the result
    print("BMI: {:.2f}".format(bmi))
    print("Category: {}".format(category))

# Run the program
if __name__ == "__main__":
    main()


