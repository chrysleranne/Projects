import time
name = input ("Hi, What is your name? ").title()
print(f"WELCOME {name}, TO MY CODE COMPILER PROGRAM!")
print("===========================================")

while True:
    print("\nMENU LIST")
    print("\n===========================================")
    print("\nA - Print Statements")
    print("B - Variables")
    print("C - Operators")
    print("D - Conditional Statements")
    print("E - Loop")
    print("F - List")
    print("G - Functions")
    print("X - Exit")

    choice = input("\nInput your choice:  ").upper()

    if choice == "A":
        while True:
            print("\nOption 1 Submenu: ")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            sub_choice = input("\nEnter your choice:  ")
            if sub_choice == 'a':
                print("\n\t===========================================")
                print(" \n\t A print statement is a command used in\n\t programming to output or display information\n\t such as text, numbers, or variables to the\n\t screen, console, or terminal.")
                print("\n\t===========================================")
                continue
            elif sub_choice == 'b':
                print("\n\t===========================================")
                print("\n\tExample: print('Hi welcome to the Python world')")
                print("\n\t===========================================")
                continue
            elif sub_choice == 'c':
                print("\n\t=======================")
                print("\n\t  Wait for a while...")
                print("\n\t=======================")
                time.sleep(1.5)


                break
            else:
                print("\nInvalid choice. Please enter a, b, or c.")

                continue

    elif choice == "B":
        print("\nPlease Wait....")
        
        while True:
            print("\nOption 2 Submenu: ")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            sub_choice = input("\nEnter your choice:  ")
            if sub_choice == 'a':
                print("\n\t================================================")
                print("\n\tVariable can change or update its value anytime.\n\tProgrammers use variables to keep track of important\n\tdata, like a score in a game or a\n\tuser's name.")
                print("\n\t================================================")

                continue
            elif sub_choice == 'b':
                print("\nExample:")
                print("\nINPUT:")
                print("name = input('What is your name? ')")
                print("age = input(\"How old are you? \")")
                print("\n\tHello, name!")
                print("\n\tYou are age years old.")

                print("\nOUTPUT:")
                name = input("What is your name? ")
                age = input("How old are you? ")

                print("\n\t================================")
                print("\n\tHello,", name + "!")
                print("\n\tYou are", age, "years old.")
                print("\n\t================================")


                continue
            elif sub_choice == 'c':
                print("\nWait for a while....")
                time.sleep(1.5)
                break
            else:
                print("Invalid choice... Please enter a, b, or c.")

                continue
    elif choice == "C":
        print("\nPlease Wait....")

        while True:
             print("\nOption 3 Submenu: ")
             print("a - Definition")
             print("b - Example")
             print("c - Back to Main Menu")

             sub_choice = input("\nEnter your choice: ")
             if sub_choice == 'a':
                 print("\n\t====================================================")
                 print("\n\tOperators do math or compare things, like + or ==.\n\tThey help a program solve problems, check conditions,\n\tor combine values.")
                 print("\n\t====================================================")

                 continue
             elif sub_choice == 'b':
                 print("\nExample: ")
                 print("\nINPUT: ")
                 num1 = int(input("Enter the first number: "))
                 num2 = int(input("Enter the second number: "))

                 print("\n\t=============================================")
                 print("\n\tAddition:", num1, "+", num2, "=", num1 + num2)
                 print("\tSubtraction:", num1, "-", num2, "=", num1 - num2)
                 print("\tMultiplication:", num1, "*", num2, "=", num1 * num2)
                 print("\tDivision:", num1, "/", num2, "=", num1 / num2)
                 print("\tIs the first number greater than the second?", num1 > num2)
                 print("\tAre the numbers equal?", num1 == num2)
                 print("\n\t=============================================")   

                 continue
             elif sub_choice == 'c':
                print("\nWait for a while....")
                time.sleep(1.5)
                 
                break
             else:
                print("Invalid choice. Please enter a,b, or c.")
            
                continue

        
    elif choice == "D":
        while True:
            print("Option 4 Submenu:")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            sub_choice=input("\nInput Your Choice: ")
            if sub_choice == 'a':
                print("\n\t======================================================")
                print("\n\tIf statements check conditions and run code if true.\n\tThey tell the program to do something only when\n\ta certain condition is true. If the condition\n\tis not true, the program can do something else\n\tusing else.")
                print("\n\t======================================================")

                continue

            elif sub_choice =='b':
                print("\nExample: ")
                print("\nINPUT:")
                print('\n\tage = int(input("\Enter your age: "))')
                print('\tif age >= 18:')
                print('\t    print("You are an adult!")')
                print('\telse:')
                print('\t    print("You are a minor.")')

                print("\nOUTPUT: ")
                print("\n\t==================================")
                age = int(input("\n\tEnter your age: "))
                
                if age >= 18:
                    print("\tYou are an adult!")
                else:
                    print("\tYou are a minor.")
                print("\n\t===================================")

                continue
            
            elif sub_choice =='c':
                print("Please Wait....")
                 
                break
            else:
                print("Invalid choice. Please enter a,b, or c.")
            
                continue 

        continue
    elif choice == "E":
       while True:
            print("\nOption 5 Submenu: ")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            sub_choice = input("Enter your choice: ")
            if sub_choice == 'a':
                print("Loops repeat code many times.")
                continue
            elif sub_choice == 'b':
                print("Example:\nfor i in range(2):\n    print(i)  # Shows: 0 1")
                continue
            elif sub_choice == 'c':
                print("Please Wait....")
                 
                break
            else:
                print("\nInvalid choice. Please enter a, b, or c.")
                continue

    elif choice == "F":
        while True:
            print("\nOption 6 Submenu: ")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            sub_choice = input("Enter your choice: ")
            if sub_choice == 'a':
                print("Lists hold many items in order.")

                continue

            elif sub_choice == 'b':
                print("Example: my_list = [1, 2]; print(my_list[0])  # Shows: 1")

                continue

            elif sub_choice == 'c':
                print("Please Wait....")
                 
                break

            else:
                print("\nInvalid choice. Please enter a, b, or c.")
                continue

    elif choice == "G":
        while True:
            print("\nOption 7 Submenu: ")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            sub_choice = input("Enter your choice: ")
            if sub_choice == 'a':
                print("Functions are code blocks that do tasks.")
                
                continue
            
            elif sub_choice == 'b':
                print("Example:\ndef say_hi():\n    print('Hi')\nsay_hi()  # Shows: Hi")

                continue
 
            elif sub_choice == 'c':
                print("Please Wait....")
                 
                break

            else:
                print("\nInvalid choice. Please enter a, b, or c.")
                continue


    elif choice == "X":
        print("System Out. Thank you for using the compiler program!")

        break 
    
    else:
        print(" Invalid choice. Please select from the menu options (A-G, X).")
        continue 
