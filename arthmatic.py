

def menu():
    print("1.for addition operations")
    print("2.for substraction operations")
    print("3.for multiplications operations")
    print("4.for Division operations")
    print("5.exit")
    
    try:
        selection = int(input("Enter you choice"))

        if selection == 1:
            addition()
        elif selection == 2:
            substraction()
        elif selection == 3:
            multiplication()
        elif selection == 4:
            division()
        elif selection == 5:
            exit()
    except ValueError:
        print("you enter Wrong Choice Enter value between 1 -5")
        menu()


def addition():
    print("Enter Numbers For Addition")
    a = int(input())
    b = int(input())
    add = int(a) + int(b)
    print("your addition = ")
    print(add)
    key = input("enter something to go further")
    menu()

def substraction():
    print("Enter Numbers For substraction")
    a = int(input())
    b = int(input())
    substraction = int(a) - int(b)
    print("your substraction = ")
    print(substraction)
    key = input("enter something to go further")
    menu()

def multiplication():
    print("Enter Numbers For multiplication")
    a = int(input())
    b = int(input())
    multiplication = int(a) * int(b)
    print("your multiplication = ")
    print(multiplication)
    key = input("enter something to go further")
    menu()

def division():
    print("Enter Numbers For division")
    a = int(input())
    b = int(input())
    division = int(a) / int(b)
    print("your division = ")
    print(division)
    key = input("enter something to go further")
    menu()

def exit():
    exit

menu()


    





