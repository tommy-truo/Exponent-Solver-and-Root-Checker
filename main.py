import os


def clear_console():
    if os.name == 'nt':
        os.system('cls')
    
    else:
        os.system('clear')


def main_menu():
    print("1. Find Value of an Exponent\n2. Check for N'th Root of a Number")
    
    menu_choice = input("\nWhat would you like to do?\n>>>> ")

    if menu_choice == "1":
        find_exp_value()

    elif menu_choice == "2":
        check_for_perfect_root()

    else:
        clear_console()

        print("Please enter a valid option.\n")

        main_menu()


def get_radicand():
    radicand = input("What is the number to be checked?\n>>>> ")

    while True:
        try:
            float(radicand)

            break

        except ValueError:
            clear_console()

            print("Please enter a valid number.")

            radicand = input("\nWhat is the number to be checked?\n>>>> ")

    return float(radicand)


def get_index():
    index = input("\nWhat is the index (n'th root) of the radical?\n>>>> ")

    while True:
        try:
            float(index)

            break

        except ValueError:
            clear_console()

            print("Please enter a valid number.")

            index = input("\nWhat is the index (n'th root) of the radical?\n>>>> ")

    return float(index)


def check_for_perfect_root():
    radicand = get_radicand()

    index = get_index()

    root = radicand ** (1./index)

    if abs(index) % 10 == 1:
        print("\n\nThe {}st root of {} is {}".format(index, radicand, root))

    elif abs(index) % 10 == 2:
        print("\n\nThe {}nd root of {} is {}".format(index, radicand, root))

    elif abs(index) % 10 == 3:
        print("\n\nThe {}rd root of {} is {}".format(index, radicand, root))

    else:
        print("\n\nThe {}th root of {} is {}".format(index, radicand, root))


def get_base_num():
    base = input("What is the base number?\n>>>> ")

    while True:
        try:
            float(base)

            break

        except ValueError:
            clear_console()
            
            print("Please enter a valid number.")

            base = input("\nWhat is the base number?\n>>>> ")

    return float(base)


def get_exp_num():
    exp = input("\nWhat is the exponent?\n>>>> ")

    while True:
        try:
            float(exp)

            break

        except ValueError:
            clear_console()
            
            print("Please enter a valid number.")

            exp = input("\nWhat is the exponent?\n>>>> ")

    return float(exp)


def find_exp_value():
    clear_console()
    
    base = get_base_num()

    exp = get_exp_num()

    value = base ** exp

    clear_console()
    
    print("The value of {} raised to the power of {} is {}.".format(base, exp, value))


def main():
    clear_console()
    
    main_menu()


if __name__ == "__main__":
    main()