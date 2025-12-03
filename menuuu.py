import time

name = input("\nHi, what is your name? ").title()
print(f"\nWelcome to the Code Compiler Program {name}! This is Chrysler your host, and here to guide you through this program.  ")

while True:
    print("\n\t===============================\n\tMAIN MENU")
    print("\tC - Exploring Print Statements")
    print("\tH - Understanding Variables")
    print("\tR - Working with Operators")
    print("\tY - Using Conditional Statements")
    print("\tS - Implementing Loops")
    print("\tL - Managing List")
    print("\tE - Defining Functions")
    print("\tX - Exiting Program")
    print("\t===============================")

    # Get input and convert it to uppercase to handle 'a' or 'A', 'x' or 'X'
    choice = input("\nInput your choice:  ").upper()

    if choice == "C":
        # Your code for Print Statements goes here
        print("Please Wait....")
        time.sleep(2)
        #upon exploring sir, I found timer that make you wait to print what you input just import time above
        while True:
            print("\nOption 1 Submenu: ")
            print("1. Print Statements Characteristics")
            print("2. Print Statements Implementation and Use Cases")
            print("3. Back to Main Menu")

            sub_choice = input("Enter your choice: ")
            if sub_choice == '1.':
                while True:
                    print("\nPrint Statements Characteristics Menu:")
                    print("a. Definition")
                    print("b. Purpose")
                    print("c. Back to Sub Menu")

                    newsub_choice = input("Enter your choice: ")

                    if newsub_choice == 'a.':
                        print("\nDefinition of Print Statements:")
                        print("In Python, a print statement is a built-in function call, written as print(), that outputs text or data to the console or terminal. It evaluates its arguments, converts them into string representations, and displays the resulting text for the user. The print function is one of the most fundamental tools in Python because it provides a simple way to communicate information from a running program to the person using or debugging it.")
                    
                    elif newsub_choice == 'b.':
                        print("\nPurpose of Print Statements:")
                        print("The primary purpose of print statements in Python is to allow programmers to observe what a program is doing at runtime. This includes viewing the values of variables, checking the flow of logic, verifying correct program execution, and presenting information to users in a readable format.")

                    elif newsub_choice == 'c.':
                        print("\nBack to Sub Menu")
                        print("\tPlease Wait . . .")
                        time.sleep(2)
                        break
                    else:
                        print("Invalid choice. Please enter a - c only.")
                    continue

            elif sub_choice == '2.':
                while True:
                    print("\nPrint Statements Implementation and Use Cases Menu:")
                    print("a. Example")
                    print("b. Usage")
                    print("c. Application")
                    print("d. Exit")

                    newsub_choice = input("Enter your choice: ")

                    if newsub_choice == 'a.':
                        print("\nExample of Print Statements:")
                        print(".....")
                    
                    elif newsub_choice == 'b.':
                        print("\nUsage of Print Statements:")
                        print("Using a print statement in Python involves calling the print() function and passing in one or more values to display. These values may include strings, numbers, variables, expressions, or formatted data. The function automatically inserts spaces between multiple arguments and ends with a newline unless otherwise specified. Programmers can also customize behavior using parameters like sep for the separator between values and end to control what appears at the end of the output.")

                    elif newsub_choice == 'c.':
                        print("\nApplication of Print Statements:")
                        print("Print statements are applied in debugging, testing, teaching, and simple user-interface outputs. They are used in virtually all Python programs when immediate visual information is needed.")

                    elif newsub_choice == 'd.':
                        print("\nBack to Sub Menu")
                        print("\tPlease Wait . . .")
                        time.sleep(2)
                        break
                    else:
                        print("Invalid choice. Please enter a - d only.")

            elif sub_choice == '3.':
                print("\nExiting, back to main menu.\n\tPlease Wait . . .")
                time.sleep(2)
                break

            else:
                print("\nInvalid choice. Choose only from 1 -3.")
                continue
    elif choice == "H":
        print("\nPlease Wait....")
        time.sleep(2)
        while True:
            print("\nOption 2 Submenu: ")
            print("1. Variables Characteristics")
            print("2. Variables Implementation and Use Cases")
            print("3. Back to Main Menu")

            sub_choice = input("Enter your choice: ")
            if sub_choice == '1.':
                while True:
                    print("\nVariables Characteristics Menu:")
                    print("a. Definition")
                    print("b. Purpose")
                    print("c. Types")
                    print("d. Back to Sub Menu")

                    newsub_choice = input("Enter your choice: ")

                    if newsub_choice == 'a.':
                        print("\nDefinition of Variables:")
                        print("A variable in Python is a named reference to a value stored in memory. It allows programmers to label data so it can be reused and manipulated throughout a program.")
                    
                    elif newsub_choice == 'b.':
                        print("\nPurpose of Variables:")
                        print("The purpose of a variable is to store information that a program needs to operate on. Variables make code flexible by allowing values to change without modifying the entire program.")

                    elif newsub_choice == 'c.':
                        print("\nTypes of Variables:")
                        print(".....")

                    elif newsub_choice == 'd.':
                        print("\nBack to Sub Menu")
                        print("\tPlease Wait . . .")
                        time.sleep(2)
                        break
                    else:
                        print("Invalid choice. Please enter a - d only.")
                    continue

            elif sub_choice == '2.':
                while True:
                    print("\nVariables Implementation and Use Cases Menu:")
                    print("a. Example")
                    print("b. Usage")
                    print("c. Application")
                    print("d. Exit")

                    newsub_choice = input("Enter your choice: ")

                    if newsub_choice == 'a.':
                        print("\nExample of Variables:")
                        print("....")
                    
                    elif newsub_choice == 'b.':
                        print("\nUsage of Variables:")
                        print("......")

                    elif newsub_choice == 'c.':
                        print("\nApplication of Variables:")
                        print("Variables are applied in calculations, data processing, user input storage, program state tracking, and nearly every aspect of Python development. They enable programs to handle dynamic, changing information rather than fixed values.")

                    elif newsub_choice == 'd.':
                        print("\nBack to Sub Menu")
                        print("\tPlease Wait . . .")
                        time.sleep(2)
                        break
                    else:
                        print("Invalid choice. Please enter a - d only.")

            elif sub_choice == '3.':
                print("\nExiting, back to main menu.\n\tPlease Wait . . .")
                time.sleep(2)
                break

            else:
                print("\nInvalid choice. Choose only from 1 -3.")
                continue
    
    elif choice == "R":
        print("\nPlease Wait....")
        time.sleep(2)
        while True:
            print("\nOption 3c Submenu: ")
            print("1. Loop Characteristics")
            print("2. Loop Implementation and Use Cases")
            print("3. Back to Main Menu")

            sub_choice = input("Enter your choice: ")
            if sub_choice == '1.':
                while True:
                    print("\nLoop Characteristics Menu:")
                    print("a. Definition")
                    print("b. Purpose")
                    print("c. Types")
                    print("d. Back to Sub Menu")

                    newsub_choice = input("Enter your choice: ")

                    if newsub_choice == 'a.':
                        print("\nDefinition of Loop:")
                        print("A loop is a programming structure that allows you to repeat a set of instructions until a certain condition is met.")
                    
                    elif newsub_choice == 'b.':
                        print("\nPurpose of Loop:")
                        print("The purpose of loop is to execute a block of code repeatedly for a specified number of times or until a certain condition is met.")

                    elif newsub_choice == 'c.':
                        print("\nTypes of Loop:")
                        print(".....")

                    elif newsub_choice == 'd.':
                        print("\nBack to Sub Menu")
                        print("\tPlease Wait . . .")
                        time.sleep(2)
                        break
                    else:
                        print("Invalid choice. Please enter a - d only.")
                    continue

            elif sub_choice == '2.':
                while True:
                    print("\nLoop Implementation and Use Cases Menu:")
                    print("a. Example")
                    print("b. Usage")
                    print("c. Application")
                    print("d. Exit")

                    newsub_choice = input("Enter your choice: ")

                    if newsub_choice == 'a.':
                        print("\nExample of Loop:")
                        print("....")
                    
                    elif newsub_choice == 'b.':
                        print("\nUsage of Loop:")
                        print("Use loops when you need to perform a task repeatedly, such iterating over a list or performing a calculation multiple times.")

                    elif newsub_choice == 'c.':
                        print("\nApplication of Loop:")
                        print("Loops are commonly used in data processing, game development, and simulations.")

                    elif newsub_choice == 'd.':
                        print("\nBack to Sub Menu")
                        print("\tPlease Wait . . .")
                        time.sleep(2)
                        break
                    else:
                        print("Invalid choice. Please enter a - d only.")

            elif sub_choice == '3.':
                print("\nExiting, back to main menu.\n\tPlease Wait . . .")
                time.sleep(2)
                break

            else:
                print("\nInvalid choice. Choose only from 1 -3.")
                continue

    elif choice == "Y":
        # Your code for Conditional Statements goes here
        print("Please wait...")
        time.sleep(2)
        while True:
            print("\nOption 5 Submenu: ")
            print("1. Loop Characteristics")
            print("2. Loop Implementation and Use Cases")
            print("3. Back to Main Menu")

            sub_choice = input("Enter your choice: ")
            if sub_choice == '1.':
                while True:
                    print("\nLoop Characteristics Menu:")
                    print("a. Definition")
                    print("b. Purpose")
                    print("c. Types")
                    print("d. Back to Sub Menu")

                    newsub_choice = input("Enter your choice: ")

                    if newsub_choice == 'a.':
                        print("\nDefinition of Loop:")
                        print("A loop is a programming structure that allows you to repeat a set of instructions until a certain condition is met.")
                    
                    elif newsub_choice == 'b.':
                        print("\nPurpose of Loop:")
                        print("The purpose of loop is to execute a block of code repeatedly for a specified number of times or until a certain condition is met.")

                    elif newsub_choice == 'c.':
                        print("\nTypes of Loop:")
                        print(".....")

                    elif newsub_choice == 'd.':
                        print("\nBack to Sub Menu")
                        print("\tPlease Wait . . .")
                        time.sleep(2)
                        break
                    else:
                        print("Invalid choice. Please enter a - d only.")
                    continue

            elif sub_choice == '2.':
                while True:
                    print("\nLoop Implementation and Use Cases Menu:")
                    print("a. Example")
                    print("b. Usage")
                    print("c. Application")
                    print("d. Exit")

                    newsub_choice = input("Enter your choice: ")

                    if newsub_choice == 'a.':
                        print("\nExample of Loop:")
                        print("....")
                    
                    elif newsub_choice == 'b.':
                        print("\nUsage of Loop:")
                        print("Use loops when you need to perform a task repeatedly, such iterating over a list or performing a calculation multiple times.")

                    elif newsub_choice == 'c.':
                        print("\nApplication of Loop:")
                        print("Loops are commonly used in data processing, game development, and simulations.")

                    elif newsub_choice == 'd.':
                        print("\nBack to Sub Menu")
                        print("\tPlease Wait . . .")
                        time.sleep(2)
                        break
                    else:
                        print("Invalid choice. Please enter a - d only.")

            elif sub_choice == '3.':
                print("\nExiting, back to main menu.\n\tPlease Wait . . .")
                time.sleep(2)
                break

            else:
                print("\nInvalid choice. Choose only from 1 -3.")
                continue

    elif choice == "S":
       print("\nPlease Wait....")
       time.sleep(2)
       while True:
            print("\nOption 5 Submenu: ")
            print("1. Loop Characteristics")
            print("2. Loop Implementation and Use Cases")
            print("3. Back to Main Menu")

            sub_choice = input("Enter your choice: ")
            if sub_choice == '1.':
                while True:
                    print("\nLoop Characteristics Menu:")
                    print("a. Definition")
                    print("b. Purpose")
                    print("c. Types")
                    print("d. Back to Sub Menu")

                    newsub_choice = input("Enter your choice: ")

                    if newsub_choice == 'a.':
                        print("\nDefinition of Loop:")
                        print("A loop is a programming structure that allows you to repeat a set of instructions until a certain condition is met.")
                    
                    elif newsub_choice == 'b.':
                        print("\nPurpose of Loop:")
                        print("The purpose of loop is to execute a block of code repeatedly for a specified number of times or until a certain condition is met.")

                    elif newsub_choice == 'c.':
                        print("\nTypes of Loop:")
                        print(".....")

                    elif newsub_choice == 'd.':
                        print("\nBack to Sub Menu")
                        print("\tPlease Wait . . .")
                        time.sleep(2)
                        break
                    else:
                        print("Invalid choice. Please enter a - d only.")
                    continue

            elif sub_choice == '2.':
                while True:
                    print("\nLoop Implementation and Use Cases Menu:")
                    print("a. Example")
                    print("b. Usage")
                    print("c. Application")
                    print("d. Exit")

                    newsub_choice = input("Enter your choice: ")

                    if newsub_choice == 'a.':
                        print("\nExample of Loop:")
                        print("....")
                    
                    elif newsub_choice == 'b.':
                        print("\nUsage of Loop:")
                        print("Use loops when you need to perform a task repeatedly, such iterating over a list or performing a calculation multiple times.")

                    elif newsub_choice == 'c.':
                        print("\nApplication of Loop:")
                        print("Loops are commonly used in data processing, game development, and simulations.")

                    elif newsub_choice == 'd.':
                        print("\nBack to Sub Menu")
                        print("\tPlease Wait . . .")
                        time.sleep(2)
                        break
                    else:
                        print("Invalid choice. Please enter a - d only.")

            elif sub_choice == '3.':
                print("\nExiting, back to main menu.\n\tPlease Wait . . .")
                time.sleep(2)
                break

            else:
                print("\nInvalid choice. Choose only from 1 -3.")
                continue

    elif choice == "L":
        print("\nPlease Wait....")
        time.sleep(2)
        while True:
            print("\nOption 5 Submenu: ")
            print("1. Loop Characteristics")
            print("2. Loop Implementation and Use Cases")
            print("3. Back to Main Menu")

            sub_choice = input("Enter your choice: ")
            if sub_choice == '1.':
                while True:
                    print("\nLoop Characteristics Menu:")
                    print("a. Definition")
                    print("b. Purpose")
                    print("c. Types")
                    print("d. Back to Sub Menu")

                    newsub_choice = input("Enter your choice: ")

                    if newsub_choice == 'a.':
                        print("\nDefinition of Loop:")
                        print("A loop is a programming structure that allows you to repeat a set of instructions until a certain condition is met.")
                    
                    elif newsub_choice == 'b.':
                        print("\nPurpose of Loop:")
                        print("The purpose of loop is to execute a block of code repeatedly for a specified number of times or until a certain condition is met.")

                    elif newsub_choice == 'c.':
                        print("\nTypes of Loop:")
                        print(".....")

                    elif newsub_choice == 'd.':
                        print("\nBack to Sub Menu")
                        print("\tPlease Wait . . .")
                        time.sleep(2)
                        break
                    else:
                        print("Invalid choice. Please enter a - d only.")
                    continue

            elif sub_choice == '2.':
                while True:
                    print("\nLoop Implementation and Use Cases Menu:")
                    print("a. Example")
                    print("b. Usage")
                    print("c. Application")
                    print("d. Exit")

                    newsub_choice = input("Enter your choice: ")

                    if newsub_choice == 'a.':
                        print("\nExample of Loop:")
                        print("....")
                    
                    elif newsub_choice == 'b.':
                        print("\nUsage of Loop:")
                        print("Use loops when you need to perform a task repeatedly, such iterating over a list or performing a calculation multiple times.")

                    elif newsub_choice == 'c.':
                        print("\nApplication of Loop:")
                        print("Loops are commonly used in data processing, game development, and simulations.")

                    elif newsub_choice == 'd.':
                        print("\nBack to Sub Menu")
                        print("\tPlease Wait . . .")
                        time.sleep(2)
                        break
                    else:
                        print("Invalid choice. Please enter a - d only.")

            elif sub_choice == '3.':
                print("\nExiting, back to main menu.\n\tPlease Wait . . .")
                time.sleep(2)
                break

            else:
                print("\nInvalid choice. Choose only from 1 -3.")
                continue

    elif choice == "E":
        print("\nPlease Wait....")
        time.sleep(2)
        while True:
            print("\nOption 5 Submenu: ")
            print("1. Loop Characteristics")
            print("2. Loop Implementation and Use Cases")
            print("3. Back to Main Menu")

            sub_choice = input("Enter your choice: ")
            if sub_choice == '1.':
                while True:
                    print("\nLoop Characteristics Menu:")
                    print("a. Definition")
                    print("b. Purpose")
                    print("c. Types")
                    print("d. Back to Sub Menu")

                    newsub_choice = input("Enter your choice: ")

                    if newsub_choice == 'a.':
                        print("\nDefinition of Loop:")
                        print("A loop is a programming structure that allows you to repeat a set of instructions until a certain condition is met.")
                    
                    elif newsub_choice == 'b.':
                        print("\nPurpose of Loop:")
                        print("The purpose of loop is to execute a block of code repeatedly for a specified number of times or until a certain condition is met.")

                    elif newsub_choice == 'c.':
                        print("\nTypes of Loop:")
                        print(".....")

                    elif newsub_choice == 'd.':
                        print("\nBack to Sub Menu")
                        print("\tPlease Wait . . .")
                        time.sleep(2)
                        break
                    else:
                        print("Invalid choice. Please enter a - d only.")
                    continue

            elif sub_choice == '2.':
                while True:
                    print("\nLoop Implementation and Use Cases Menu:")
                    print("a. Example")
                    print("b. Usage")
                    print("c. Application")
                    print("d. Exit")

                    newsub_choice = input("Enter your choice: ")

                    if newsub_choice == 'a.':
                        print("\nExample of Loop:")
                        print("....")
                    
                    elif newsub_choice == 'b.':
                        print("\nUsage of Loop:")
                        print("Use loops when you need to perform a task repeatedly, such iterating over a list or performing a calculation multiple times.")

                    elif newsub_choice == 'c.':
                        print("\nApplication of Loop:")
                        print("Loops are commonly used in data processing, game development, and simulations.")

                    elif newsub_choice == 'd.':
                        print("\nBack to Sub Menu")
                        print("\tPlease Wait . . .")
                        time.sleep(2)
                        break
                    else:
                        print("Invalid choice. Please enter a - d only.")

            elif sub_choice == '3.':
                print("\nExiting, back to main menu.\n\tPlease Wait . . .")
                time.sleep(2)
                break

            else:
                print("\nInvalid choice. Choose only from 1 -3.")
                continue

    elif choice == "X":
        print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print(f"System Out. Thank you for using the compiler program, {name}!")
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        break # This is the explicit stopping point
    else:
        print("Invalid choice. Please select from the menu options.")
        continue # Jumps back to the start of the loop and re-displays the menus