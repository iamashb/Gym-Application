def main():
    while True:
        print("\n1. Create Account\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            if login():
                weight = float(input("Enter your weight (in kg): "))
                height = float(input("Enter your height (in meters): "))
                bmi = calculate_bmi(weight, height)
                print(f"Your BMI is: {bmi}")
                if 18.5 < bmi and bmi < 24.9:
                    print('Your are on Healthy Weight')
                elif 18.5 > bmi:
                    print('Your are on Underweight')
                elif 24.9 < bmi:
                    print('Your are on Overweight')
                workoutsplan()

                break
            else:
                print("Invalid username or password. Please try again.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

main()
