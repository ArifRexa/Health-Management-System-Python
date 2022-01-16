def getdate():
    import datetime
    return datetime.datetime.now()

import datetime
def gettime():
    return datetime.datetime.now()


print("********************Welcome to Health Management System********************\nWhat you want to do?\n1. Lock your routine\n2. Retrieve your routine")
inpt = int(input("Enter your choice:\n"))
if inpt == 1:
    print("For which one you want to Lock:\n1. Dawod Ibrahim\n2. Rafiun israt\n3. Robiul Islam")
    name_inpt = int(input("Enter your choice:\n"))
    if name_inpt == 1:
        print("This is for Dawod\nWhat do you want to Lock\n1. Food\n2. Exercise")
        choice_inpt = int(input("Enter your choice\n"))
        if choice_inpt == 1:
            print("This is Lock for food")

            value = input("type here\n")
            with open("dawod-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")

        else:
            print("This is Lock for exercise")

            value = input("type here\n")
            with open("dawod-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")


    elif name_inpt == 2:
        print("This is for Rafiun\nWhat do you want to Lock\n1. Food\n2. Exercise")
        choice_inpt2 = int(input("Enter your choice\n"))
        if choice_inpt2 == 1:
            print("This is Lock for food")

            value = input("type here\n")
            with open("rafiun-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        else:
            print("This is Lock for exercise")

            value = input("type here\n")
            with open("rafiun-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")



    else:
        print("This is for Robiul\nWhat do you want to Lock\n1. Food\n2. Exercise")
        choice_inpt3 = int(input("Enter your choice\n"))
        if choice_inpt3 == 1:
            print("This is Lock for food")

            value = input("type here\n")
            with open("robiul-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        else:
            print("This is Lock for exercise")

            value = input("type here\n")
            with open("robiul-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")

else:
    print("For which one you want to Retrieve:\n1. Dawod Ibrahim\n2. Rafiun Israt\n3. Robiul Islam")
    name_inpt2 = int(input("Enter your choice:\n"))
    if name_inpt2 == 1:
        print("This is for Dawod\nWhat do you want to Retrieve\n1. Food\n2. Exercise")
        choice_inpt4 = int(input("Enter your choice\n"))
        if choice_inpt4 == 1:
            print("This is Retrieve for food")

            with open("dawod-food.txt") as op:
                for i in op:
                    print(i, end="")
        else:
            print("This is Retrieve for exercise")
            with open("dawod-ex.txt") as op:
                for i in op:
                    print(i, end="")


    elif name_inpt2 == 2:
        print("This is for Rafiun\nWhat do you want to Lock\n1. Food\n2. Exercise")
        choice_inpt5 = int(input("Enter your choice\n"))
        if choice_inpt5 == 1:
            print("This is Retrieve for food")

            with open("rafiun-food.txt") as op:
                for i in op:
                    print(i, end="")
        else:
            print("This is Retrieve for exercise")

            with open("rafiun-ex.txt") as op:
                for i in op:
                    print(i, end="")


    else:
        print("This is for Robiul\nWhat do you want to Lock\n1. Food\n2. Exercise")
        choice_inpt6 = int(input("Enter your choice\n"))
        if choice_inpt6 == 1:
            print("This is Retrieve for food")

            with open("robiul-food.txt") as op:
                for i in op:
                    print(i, end="")
        else:
            print("This is Retrieve for exercise")

            with open("robiul-ex.txt") as op:
                for i in op:
                    print(i, end="")
