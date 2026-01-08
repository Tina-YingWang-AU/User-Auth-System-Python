# =============================================================================================================================================================
# Gelos Enterprises User Management System
# Program Filename: "GelosLoginApplication.py"
# Data Filename: "accounts.txt"
# Purpose of program: It creates a simple menu system that incorporates 3 components and will allow the user to:
#                     1. Register a new user
#                     2. View accounts after successfully logged in
#                     3. Exit the program
# Programmer: Ying Wang
# Date: 7 November 2025
# ============================================================================================================================================================

import GelosLibraries  # import user-defined library (GelosLibraries.py)
import sys  # import Python's built-in sys module to exit the program


# Define a Function to display menu below
def DisplayMenu():
    print("""
    Gelos Enterprises User Management System
    ========================================
                   Options
                   =======
            1. Register a new user
            2. View accounts
            3. Exit
            """)
    option = input("\nEnter your option please [1, 2, or 3]: ")
    return option  # Return the value of “option”


# Define the main() Function below
def main():  # This is the main program

    print("\nWelcome to Gelos Enterprises User Management System!")
    print("Please choose an option from the menu below.")

    opt = DisplayMenu().strip()  # Call the DisplayMenu Function. strip(): to remove leading and trailing spaces of the string

    match opt:  # Use match case here as a short-cut version of multiple ifs (Matching the value of "opt")
        case "1":  # In case opt = "1"
            print("\nNew User Registration")
            print("-" * 21)
            GelosLibraries.Registration()  # Call Registration() Function from user-defined library (GelosLibraries.py)
            input(
                "\nPlease enter <Enter> key to Return to Menu: ")  # Use a false input command to wait for the user to press Enter
            main()  # Run the main() function (main() function calls itself recursively)
        case "2":
            print("\nDisplaying Registered Users")
            print("-" * 27)
            print("\n[Please note you have to be a registered user in the system.]")
            GelosLibraries.viewAccounts()  # Call viewAccounts() Function from user-defined library (GelosLibraries.py)
            input(
                "\nPlease enter <Enter> key to Return to Menu: ")  # Use a false input command to wait for the user to press Enter
            main()  # Run the main() function (main() function calls itself recursively)
        case "3":
            while True:
                checkExit = input("\nConfirm exit: Are you sure you want to exit the application? [y/n]: ")
                if checkExit.strip().lower() != "y" and checkExit.strip().lower() != "n":
                    print("\nInvalid input. Please try again with 'y' or 'n' only.")
                    continue
                else:
                    break

            if checkExit.strip().lower() == "y":
                print("\nYou chose to exit. Thank you, Program ended..")
                sys.exit()  # sys.exit(): a function in Python's sys module used to terminate the execution of a Python program
            else:
                print("\nYou have chosen not to exit the application.")
                input("\nPlease enter <Enter> key to Return to Menu: ")
                main()

        case _:  # If user enter something other than "1", "2" or "3"
            print("\nError: Invalid Option number entered!")
            input(
                "\nPlease press <Enter> key to Return to Menu: ")  # Use a false input command to wait for the user to press Enter
            main()  # Run the main() function (main() function calls itself recursively)


# Call the Main Function
main()  # This will carry out the whole application
# End of Program
