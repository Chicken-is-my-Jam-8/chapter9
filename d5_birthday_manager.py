
b_dict = {}

def main():

    main_menu()

def main_menu():
    
    menu_on = 1
    while menu_on == 1:
        print()
        print("Birthday Manager")
        print("1. Add a Birthday")
        print("2. View a Birthday")
        print("3. Display all Birthdays")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_birthday()
        elif choice == 2:
            view_birthday()
        elif choice == 3:
            display_birthdays()
        elif choice == 4:
            menu_on = 0
        else:
            print("Invalid input: please enter an integer from 1 - 4")

def add_birthday():
    name = input("Enter friend's name: ")
    date = input("Enter birthday (e.g., YYYY-MM-DD): ")
    b_dict[name] = date
    print(f"{name}'s birthday has been added!")

def view_birthday():
    v_name = input("enter the name of the friend whose birthday you want to view: ")
    v_date = b_dict[v_name]
    print(f"{v_name}'s birthday is on {v_date}")

def display_birthdays():
    for x,y in b_dict.items():
        print()
        print(f"{x}'s birthday is on {y}")


main()
