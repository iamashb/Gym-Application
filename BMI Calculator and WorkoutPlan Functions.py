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
