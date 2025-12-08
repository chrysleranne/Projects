print("WELCOME TO MY CODE COMPILER PROGRAM\n=============================================")

while True:
    print("MENU LIST\n====================================")
    print("A - Print Statements")
    print("B - Variables")
    print("C - Operators")
    print("D - Conditional Statements")
    print("E - Loop")
    print("F - List")
    print("G - Functions")
    print("X - Exit")

    choice = input("Input your choice:  ").upper()

    if choice == "A":
        while True:
            print("\nOption 1 Submenu: ")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            sub_choice = input("Enter your choice:  ")
            if sub_choice == 'a':
                print(".....")

                continue
            elif sub_choice == 'b':
                print("....")

                continue
            elif sub_choice == 'c':
                print("Please Wait....")


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

            sub_choice = input("Enter your choice:  ")
            if sub_choice == 'a':
                print("....")

                continue
            elif sub_choice == 'b':
                print(".....")

                continue
            elif sub_choice == 'c':
                print("\nPlease Wait....")
                 
                break
            else:
                print("Invalid choice. Please enter a, b, or c.")

                continue
    elif choice == "C":
        print("\nPlease Wait....")

        while True:
             print("\nOption 3 Submenu: ")
             print("a - Definition")
             print("b - Example")
             print("c - Back to Main Menu")

             sub_choice = input("Enter your choice: ")
             if sub_choice == 'a':
                 print("....")

                 continue
             elif sub_choice == 'b':
                 print("....")

                 continue
             elif sub_choice == 'c':
                print("\nPlease Wait....")
                 
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

            sub_choice=input("Input Your Choice")
            if sub_choice == 'a':
                pass

                continue

            elif sub_choice =='b':
                pass

                continue
            
            elif sub_choice =='c':
                pass
                 
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
                pass
                continue
            elif sub_choice == 'b':
                pass
                continue
            elif sub_choice == 'c':
                pass
                 
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
                pass
                continue

            elif sub_choice == 'b':
                pass

                continue

            elif sub_choice == 'c':
                pass
                 
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
                pass
                
                continue
            
            elif sub_choice == 'b':
               pass

                continue
 
            elif sub_choice == 'c':
                pass
                 
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

