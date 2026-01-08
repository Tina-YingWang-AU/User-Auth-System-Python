# =============================================================================================================================
# Program Filename: "GelosLibraries.py"
# Data Filename: "accounts.txt"
# Purpose of program: It contains user define functions for user registration (component 1), logging in (component 2) and displaying existing users (component 3).
# Programmer: Ying Wang
# Date: 7 November 2025
# =============================================================================================================================

import csv  # import Python's built-in CSV module to handle CSV files
import sys  # import Python's built-in sys module to exit the program


# Component 1 - Create a new user account (registration)
def Registration():  # Define a Function for user registration

    while True:  # Start an Open Loop to allow Continuation of another user registration
        # Block of code to deal with username entry
        while True:  # This is an open loop. If the user entered a username which already exists in accounts.txt, ask them to re-enter until it hasn't existed in the file.
            checkUName = False  # declare a flag variable checkUName to check if the username the user entered already exists in the file, set it to False initially to enter the while loop
            while True:  # This is an open loop. If user entered an empty username, ask them to re-enter until a non-empty username is entered.

                newUserName = input("\nPlease enter your new username: ")  # Ask user to enter a new username

                if newUserName.strip() == "":  # If the trimmed version of username the user entered is empty, display an error message. strip(): to remove any leading and trailing spaces of the string
                    print("\nError: you entered an empty username. Please try again with a non-empty username.")
                    continue  # return the user back to the beginning of this while loop to re-enter a new username
                else:
                    break  # If the username the user entered is not empty, get out of this while loop

            # This block of code is to check if the username the user entered already exists in "accounts.txt" file
            # Exception handling is added below - if there are file-related errors, display error message and exit Registration () function
            try:  # if "accounts.txt" text file can be accessed, execute following block of code

                with open("accounts.txt", "r") as csvFile:  # Open "accounts.txt" text file in Read Mode
                    csvReader = csv.reader(csvFile,
                                           delimiter=",")  # Creates a CSV reader object that splits each line into a list using a comma as the separator
                    for field in csvReader:  # Loops through each line in the file, one at a time
                        if field != "":  # if that line is not empty (to avoid errors if there are blank lines)
                            if newUserName.strip().lower() == field[
                                0].strip().lower():  # If the lowercased and trimmed version of username matches lowercased and trimmed version of record in accounts.txt, set flag variable checkUName to True
                                # strip(): to remove leading and trailing spaces of the string. lower(): to convert string to lowercase
                                checkUName = True
                                break  # if a match is found, get out of this loop

            except (FileNotFoundError, PermissionError, OSError,
                    csv.Error):  # If there are file-related errors, display error message and exit Registration () function. OSError: for general file system issues (e.g. disk error, path problems); csv.Error: error related to reading or writing csv data
                print("\nError: User Database issue. Please contact your administrator.")
                return  # exit Registration () function

            if checkUName:  # If there is a match between the username the user entered and the record in "accounts.txt", display an error message to warn that the username is taken
                # print("\nError: This username already exists. Please try again with a different username.")
                while True:
                    checkUN = input("\nError: This username already exists. Would you like to try again? [y/n]: ")
                    if checkUN.strip().lower() != "y" and checkUN.strip().lower() != "n":
                        print("\nError: Invalid input. Please try again with 'y' or 'n' only.")
                        continue
                    else:
                        break

                if checkUN.strip().lower() == "y":
                    print("\nYou have chosen to proceed. Please try again with another username.")
                    continue
                else:
                    print("\nYou have chosen not to proceed with registration. Thank you.")
                    return

            else:  # Otherwise, display a message indicating that username is available and get out of this loop
                print("\nThis username is available. You can proceed with registration.")
                break  # Get out of this while loop

        # Block of code to deal with password entry
        while True:  # This is an open loop. If the password user entered is shorter than 10 characters, ask the user to re-enter a password again until it meets the minimum length requirement.

            newPassword = input(
                "\nPlease enter your new password (it must be minimal 10 characters long and can include any characters): ")  # Ask user to enter a password

            if len(newPassword) >= 10:  # Check if the password length is greater or equal to 10 characters. len(): returns the number of characters in the string
                break  # If the password meets the length requirement, get out of the loop
            else:
                while True:
                    checkPW = input(
                        "\nInvalid password length: it must be minimal 10 characters long. Would you like to try again? [y/n]: ")

                    if checkPW.strip().lower() != "y" and checkPW.strip().lower() != "n":
                        print("\nError: Invalid input. Please try again with 'y' or 'n' only.")
                        continue
                    else:
                        break

                if checkPW.strip().lower() == "y":
                    print("\nYou have chosen to proceed. Please try again with another password.")
                    continue
                else:
                    print("\nYou have chosen not to proceed with registration. Thank you.")
                    return

        while True:

            confirmPW = input("\nPlease re-enter your password to confirm: ")

            if confirmPW == newPassword:
                print("\nPassword confirmed. Proceeding with your registration.")
                dataRecord = newUserName + "," + newPassword + "\n"  # if new valid username and password has been entered, join both string data separated by comma to make one record
                break
            else:
                while True:
                    checkConfirmPW = input("\nError: Passwords do not match. Would you like to try again? [y/n]: ")
                    if checkConfirmPW.strip().lower() != "y" and checkConfirmPW.strip().lower() != "n":
                        print("\nError: Invalid input. Please try again with 'y' or 'n' only.")
                        continue
                    else:
                        break

                if checkConfirmPW.strip().lower() == "y":
                    print("\nYou have chosen to proceed. Please try again to confirm your password.")
                    continue
                else:
                    print("\nYou have chosen not to proceed with registration. Thank you for confirming.")
                    return

        # Exception handling is added below - if there are file-related errors, display error message and exit Registration() function
        try:  # if no file-related errors, execute following block of code
            with open("accounts.txt",
                      "a+") as file:  # Open "accounts.txt" text file in Append mode, plus sign "+" means that it will create a new file if it does not exist
                file.write(
                    dataRecord)  # Write the data record of new valid username and password into "accounts.txt" file
        except (FileNotFoundError, PermissionError, OSError,
                csv.Error):  # If there are file-related errors, display error message and exit Registration () function. OSError: for general file system issues (e.g. disk error, path problems); csv.Error: error related to reading or writing csv data
            print(
                "\nError: Cannot save user information to database. Registration failed. Please contact administrator.")
            return  # exit Registration() function

        while True:  # This is an open loop. When checking if user wants to register another account, if the user entered something other than "y"/"Y" or "n"/"N", ask them to re-enter until valid response is given.

            check = input(
                f"\nYou have successfully registered a new user account. Would you like to register another user account? [y/n]: ")  # Check if the user wants to register for another account

            if check.lower() != "y" and check.lower() != "n":  # lower(): convert the string to lowercase.
                print("\nError: Invalid input. Please try again with 'y' or 'n' only.")
                continue  # return user back to beginning of the loop
            else:
                break  # If valid response is given, get out of this while loop

        if check.lower() == "n":  # lower(): convert string to lowercase
            print(
                "\nYou have chosen not to register another user account. Thank you for registering. Your registration is complete.")
            return  # exit Registration() function
        else:
            print("\nYou have chosen to register another user account. Please continue.")
            continue  # if the user chose to register another account, return them back to the beginning of this while loop to start a new registration


# Component 2 - Check a username and password (logging in)
# Only when user enter a username that matches one record of "accounts.txt", and they enter this username 3 consecutive times, program would end.
def userLogin():  # Define a Function for user login

    maximumAttempts = 3  # Maximum number of consecutive failed login attempts

    compareList = []

    lockList = []
    while True:

        checkLogin = False  # set a flag variable checkLogin to check if the credentials the user entered match a valid entry in "accounts.txt"

        while True:  # if the username is locked, allow another try with different username
            ckLock = False

            while True:  # This is an open loop to validate username input to ensure it is not empty. If user entered an empty username, ask them to re-enter again until a non-empty username is entered

                UName = input("\nPlease enter your username: ")  # Ask user to enter a username

                if UName.strip() == "":  # If the user entered an empty username, display an error message. strip(): to remove leading and  spaces of string
                    print("\nYou entered an empty username. Please try again with a non-empty username.")
                    continue  # return the user back to the beginning of this while loop to re-enter a new username
                else:
                    break  # If the username the user entered is not empty, get out of this while loop

            try:
                with open("lockUserList.txt", "r+") as lockfile:
                    csvReader = csv.reader(lockfile)
                    for row in csvReader:
                        if row != "" and len(row) > 0 and row[0].strip():
                            if UName.strip().lower() == row[0].strip().lower():
                                ckLock = True
                                break

            except (FileNotFoundError, csv.Error, PermissionError, OSError):
                print("\nError: User Database issue. Please contact your administrator.")
                return False

            if ckLock:
                while True:
                    checkLoginifLock = input(
                        "\nSorry, this account has been locked. Please contact the administrator for assistance. Would you like to log in another account? (y/n): ")

                    if checkLoginifLock.strip().lower() != "y" and checkLoginifLock.strip().lower() != "n":
                        print("\nError: Invalid input. Please try again with 'y' or 'n' only.")
                        continue
                    else:
                        break

                if checkLoginifLock.strip().lower() == "y":
                    print("\nYou have chosen to proceed. Please try again with another username.")
                    continue
                else:
                    print("\nYou have chosen not to proceed. Thank you.")

                    return False
            else:
                break

        while True:  # This is an open loop to validate password input to ensure it is not empty. If user entered an empty password, ask them to re-enter again until a non-empty password is entered

            PWord = input("\nPlease enter your password: ")  # Ask user to enter a password

            if PWord == "":  # If the user entered an empty password, display an error message
                print("\nYou entered an empty password. Please try again with a non-empty password.")
                continue  # return the user back to the beginning of this while loop to re-enter a new password
            else:
                break  # If the password the user entered is not empty, get out of this while loop

        # Exception handling is added below - If there are file-related errors, display error message, exite userLogin() function and return False, 0
        try:  # if no file-related errors, execute following block of code
            with open("accounts.txt", "r") as csvfile:  # Open "accounts.txt" text file in Read Mode
                csvReader = csv.reader(csvfile,
                                       delimiter=",")  # Creates a CSV reader object that splits each line into a list using a comma as the separator.

                for field in csvReader:  # Loop to check each line in the file for matching credentials. Loops through each line in the file, one at a time
                    if field != "":  # If that line is not empty (to avoid errors if there are blank lines)
                        if UName.strip().lower() == field[0].strip().lower() and PWord == field[
                            1]:  # if the password and lowercased and trimmed version of username the user entered matches record in "accounts.txt", set checkLogin to True
                            # strip(): to remove the leading and trailing spaces of string. lower(): convert the string to lowercase
                            checkLogin = True  # set the flag variable checkLogin to True if credentials match
                            break  # If a match is found, get out of this for loop
                if not checkLogin:
                    compareList.append(UName.strip())


        except (FileNotFoundError, PermissionError, OSError,
                csv.Error):  # If there are file-related errors, display error message and exit userLogin() Function

            print("\nError: User Database issue. Please contact your administrator.")
            return False  # exit userLogin() function and return False

        # This block of code is to process the login result
        if checkLogin:  # If the credentials the user entered match a valid entry in "accounts.txt" file, display a "Logged in successful" message, exit userLogin() function and return True
            print("\nYou have successfully logged in.")

            return True  # Login successful, exit userLogin() function and return results

        else:
            checkForLogin = False

            i = 0

            while i < len(compareList) - 2:

                if compareList[i] == compareList[i + 1] == compareList[i + 2]:
                    checkPrevious = (i == 0 or compareList[i - 1] != compareList[i])
                    checkNext = (i == len(compareList) - 3 or compareList[i + 3] != compareList[i])
                    if checkPrevious and checkNext:
                        with open("accounts.txt", "r") as csvfile:
                            csvReader = csv.reader(csvfile, delimiter=",")
                            for field in csvReader:
                                if field != "":
                                    if compareList[i] == field[0].strip().lower():

                                        if compareList[i].strip() not in lockList:
                                            # print("\ncompareList [i] is not in lockList")
                                            checkForLogin = True
                                            lockList.append(compareList[i])

                                            with open("lockUserList.txt", "a+") as lockfile:
                                                lockfile.write(f"{lockList[len(lockList) - 1]}\n")

                                                break

                i = i + 1

            if checkForLogin:
                print(
                    f"\nYou have reached the maximum number of consecutive login attempts - {maximumAttempts} times. Your account is now locked. Please contact administrator for help. Program ended..")
                sys.exit()

            else:
                while True:
                    checkForCont = input(
                        "\nError: invalid credentials. Would you like to try logging in again? [y/n]: ")
                    if checkForCont.strip().lower() != "y" and checkForCont.strip().lower() != "n":
                        print("\nError: Invalid input. Please try again with 'y' or 'n'.")
                        continue
                    else:
                        break

                if checkForCont.strip().lower() == "y":
                    print("\nYou have chosen to proceed. Please try logging in again.")

                    continue
                else:
                    print("\nYou have chosen not to proceed. Thank you.")
                    return False


# Component 3 - View existing accounts  (displaying users)
def viewAccounts():
    loginSuccess = userLogin()  # Call userLogin() function from Component 2 block of code

    if loginSuccess:  # If user successfully logged in, display the numbered existing usernames

        print("""\nWould you like to view users sorted by registration date or by username?
------------------------------------------------------------------------
1. By registration date (earliest first)
2. By registration date (latest first)
3. By username (A-Z)
4. By username (Z-A)""")

        while True:
            choiceViewAcc = input("\nEnter your option please [1, 2, 3, or 4]: ").strip()

            if choiceViewAcc.strip() != "1" and choiceViewAcc.strip() != "2" and choiceViewAcc.strip() != "3" and choiceViewAcc.strip() != "4":
                print("\nError: Invalid input. Please try again with '1', '2', '3' or '4' only.")
                continue
            else:
                break

        if choiceViewAcc.lower() == "1":
            print("\nAll registered user accounts are listed below sorted by registration date (earliest first).\n")

            count = 0  # Initialized the counter for username display

            with open("accounts.txt", "r") as csvfile:  # Open "accounts.txt" text file in Read Mode

                csvReader = csv.reader(csvfile,
                                       delimiter=",")  # Creates a CSV reader object that splits each line into a list using a comma as the separator
                for field in csvReader:  # Loops through each line in the file, one at a time
                    if field != "":  # If that line is not empty (to avoid errors if there are blank lines)
                        print(
                            f"{count + 1}. {field[0].strip()}")  # Display the numbered existing username. strip(): to remove the leading and trailing spaces of the string
                        count += 1  # Increment the counter to keep track of the number of non-empty lines (usernames)

            print(f"\nTotal users = {count}")

        elif choiceViewAcc.lower() == "2":
            print("\nAll registered user accounts are listed below sorted by registration date (latest first).\n")

            NewList = []

            with open("accounts.txt", "r") as csvfile:
                csvReader = csv.reader(csvfile, delimiter=",")
                for field in csvReader:
                    if field != "":
                        NewList.append(field[0].strip())

            item = len(NewList) - 1
            counter = 0

            while item >= 0:
                print(f"{counter + 1}. {NewList[item]}")
                item = item - 1
                counter = counter + 1

            print(f"\nTotal users = {counter}")


        elif choiceViewAcc.lower() == "3":

            print("\nAll registered user accounts are listed below sorted by username (A-Z).\n")

            newUserList = []

            with open("accounts.txt", "r") as csvfile:
                csvReader = csv.reader(csvfile, delimiter=",")
                for field in csvReader:
                    if field != "":
                        newUserList.append(field[0].strip())

            i = 1
            while i < len(newUserList):
                j = 0
                while j < i:
                    if newUserList[i - j].strip() > newUserList[i - j - 1].strip():
                        break
                    else:
                        transit = newUserList[i - j - 1].strip()
                        newUserList[i - j - 1] = newUserList[i - j].strip()
                        newUserList[i - j] = transit
                        j = j + 1
                i = i + 1

            countForNewUser = 0

            for user in newUserList:
                print(f"{countForNewUser + 1}. {user}")
                countForNewUser += 1

            print(f"\nTotal users = {countForNewUser}")

        else:
            print("\nAll registered user accounts are listed below sorted by username (Z-A).\n")

            newUserList = []

            with open("accounts.txt", "r") as csvfile:
                csvReader = csv.reader(csvfile, delimiter=",")
                for field in csvReader:
                    if field != "":
                        newUserList.append(field[0].strip())

            i = 1
            while i < len(newUserList):
                j = 0
                while j < i:
                    if newUserList[i - j].strip() < newUserList[i - j - 1].strip():
                        break
                    else:
                        transit = newUserList[i - j - 1].strip()
                        newUserList[i - j - 1] = newUserList[i - j].strip()
                        newUserList[i - j] = transit
                        j = j + 1
                i = i + 1

            countForNewUser = 0

            for user in newUserList:
                print(f"{countForNewUser + 1}. {user}")
                countForNewUser += 1

            print(f"\nTotal users = {countForNewUser}")

    else:
        print(
            "\nLogin failed. Access to view accounts denied.")  # If user login failed before reaching maximum attempts, display error message
