def create_account():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    file=open('accounts.txt', 'a')
    text=file.write(f"{username}:{password}\n")

    print("Account created successfully!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    file = open('accounts.txt', 'r')
    accounts = file.readlines()
    file.close()
    for account in accounts:
        stored_username, stored_password = account.strip().split(':')
        if username == stored_username and password == stored_password:
            return True

    return False


def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


def workoutsplan ():
    need=input("If you want lose weight press 1\nIf you want gain weight press 2\nenter here: ")
    if need=='1':
        level=input("\nwhat is your current level\n1-Beginner\n2-Intermediate\n3-Advanced\nenter here: ")
        if level=='1':
            file = open("workouts1.txt", "r")
            text = file.read()
            print(text)
            file.close()
        elif level=='2':
            file = open("workouts2.txt", "r")
            text = file.read()
            print(text)
            file.close()
        elif level=='3':
            file = open("workouts3.txt", "r")
            text = file.read()
            print(text)
            file.close()
        else:
            print("Invalid choice. Please try again.")
    elif need=='2':
        level = input("\nwhat is your current level\n1-Beginner\n2-Intermediate\n3-Advanced\nenter here: ")
        if level =='1':
            file = open("workouts4.txt", "r")
            text = file.read()
            print(text)
            file.close()
        elif level =='2':
            file = open("workouts5.txt", "r")
            text = file.read()
            print(text)
            file.close()
        elif level == '3':
            file = open("workouts6.txt", "r")
            text = file.read()
            print(text)
            file.close()
        else:
            print("Invalid choice. Please try again.")
    else:
        print("Invalid choice. Please try again.")


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


