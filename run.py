from user import User
from credentials import Credentials

def login_user(username, password):
    check_user =  User.verify_user(username, password)
    return check_user

def create_new_user(username, password):
    new_user = User(username, password)
    return new_user

def save_users(user):
    user.save_user()

def delete_saved_user(user):
    user.delete_user()

def display_login_details():
    return User.display_user()

def create_new_credential(accountName, accountUsername, accountPassword):
    new_credential = Credentials(accountName, accountUsername, accountPassword)
    return new_credential

def save_new_credential(credential):
    credential.save_credentials()

def display_credential_details():
    return Credentials.display_credentials()

def delete_saved_credential(credential):
    credential.delete_credentials()

def auto_generate_password():
    return Credentials.generate_password()

def verify_cred(credential):
    return Credentials.verify_credential_exist(credential)

def search_cred(credential):
    return Credentials.search_saved_credential(credential)


def passlocker():
    print("------------------------------------------------------------------------------------------------------------------------ ")
    print("██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░  ██╗░░░░░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░ ")
    print("██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗  ██║░░░░░██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗ ")
    print("██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║  ██║░░░░░██║░░██║██║░░╚═╝█████═╝░█████╗░░██████╔╝ ")
    print("██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║  ██║░░░░░██║░░██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗ ")
    print("██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝  ███████╗╚█████╔╝╚█████╔╝██║░╚██╗███████╗██║░░██║ ")
    print("╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░  ╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝ ")
    print("------------------------------------------------------------------------------------------------------------------------ ")
    print("\n")

    print("Welcome To Password Locker")
    print("**************************")
    while True:
        print("Please choose one of the following shortcodes to continue:")
        print("NA - Create A New Account")
        print("LG - Login To Your Account")
        print("EX - Exit Application")
        print("\n")
        option = input("Your Choice: ").upper()
        print("\n")

        if option == 'NA':
            print("REGISTER")
            print("********")
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            confirm_password = input("Confirm password: ")
            save_users(create_new_user(username, password))
            
            while password != confirm_password:
                print("\n")
                print("Password Mismatch! Please Try Again")
                password = input("Enter a password: ")
                confirm_password = input("Confirm password: ")
            
            else:
                print("\n")
                print("********************************************************************")
                print("Registration Successful!! Welcome Aboard. Your Registration Details:")
                print("********************************************************************")
                print("Username: ", username, "\nPassword: ", password)
                print("\n")
                print("You can log in. Choose LG to proceed\n")
                
        elif option == 'LG':
            print("LOG IN")
            print("******")
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            login = login_user(username, password)
            print("\n")
            print("**************************************************************")
            print("Login Successful!! Welcome Back To Password Locker", username)
            print("**************************************************************")
            print("\n")
            while True:
                if login:
                    print("Dashboard Menu")
                    print("**************")
                    print("Please choose one of the following shortcodes to get continue:")
                    print("NC - Create A New Credential")
                    print("LD - Display Login Detials")
                    print("DS - Display All Saved Credentials")
                    print("FC - Find Credential")
                    print("DC - Delete A Saved Credential")
                    print("LO - Logout Application")
                    print("\n")
                    option = input("Your Choice: ").upper()
                    print("\n")

                    if option == 'NC':
                        print("NEW CREDENTIAL")
                        print("**************")
                        accountName = input("Enter the platform name: ")
                        accountUsername = input("Enter the username: ")
                        print("Select one of the following:")
                        print("EP - For enter password")
                        print("GP - For Auto Generate password")
                        choice = input("Choice: ").upper()

                        if choice == 'EP':
                            accountPassword = input("Enter the password: ")
                        elif choice == 'GP':
                            accountPassword = auto_generate_password()
                        else:
                            print("\n")
                            print("Wrong Option! Please Try Again.")
                            print("\n")
                            break

                        save_new_credential(create_new_credential(accountName, accountUsername, accountPassword))
                        print("\n")
                        print("************************************************************")
                        print("New Credential Added Successfully!! Your Crednetial Details:")
                        print("************************************************************")
                        print("Platform Name: ", accountName ,"\nUsername: ", accountUsername ,"\nPassword: ", accountPassword)
                        print("\n")

                    elif option == 'LD':
                        if display_login_details():
                            for details in display_login_details():
                                print("Log In Details")
                                print("***************")
                                print(f"Username: {details.username} \nPassword: {details.password}")
                                print("\n")
                        else:
                            print("No Login Details Found!")

                    elif option == 'DS':
                        if display_credential_details():
                            print("Account Credentials Details")
                            print("***************************")
                            for details in display_credential_details():
                                print(f"Platfrom Name: {details.accountName} \nAccount Username: {details.accountUsername} \nPassword: {details.accountPassword}")
                                print("\n")
                        else:
                            print("No Credentials Found!")
                            print("\n")

                    elif option == 'FC':
                        platform_name = input("Enter Platform Name: ")
                        print("\n")
                        if verify_cred(platform_name):
                            search = search_cred(platform_name)
                            print("Account Credentials Details")
                            print("***************************")
                            print(f"Platfrom Name: {search.accountName} \nAccount Username: {search.accountUsername} \nPassword: {search.accountPassword}")
                            print("\n")
                        else:
                            print("\n")
                            print("The Credential Doesn't Exist!")
                            print("\n")

                    elif option == 'DC':
                        while True:
                            print("Are you sure you want to perform this action? (Y/N)\n")
                            choice = input("Choice: ").upper()
                            print("\n")
                            if choice == 'Y':
                                delete_credential = input("Enter Platform Name: ")
                                if verify_cred(delete_credential):
                                    search = search_cred(delete_credential)
                                    delete_saved_credential(search)
                                    print("\n")
                                    print("*************************************************")
                                    print(f"You have sucessfully deleted the {delete_credential} account!")
                                    print("*************************************************")
                                    print("\n")
                                else:
                                    print("\n")
                                    print("The Credential Doesn't Exist!")
                                    print("\n")
                                    break
                                break

                            elif choice == 'N':
                                break
                            else:
                                print("Wrong option! Try again")

                    elif option == 'LO':
                        print("************************")
                        print("Successfully Logged Out!")
                        print("************************")
                        print("\n")
                        break

                    else:
                        print("Wrong Option! Please Try Again.")
                        print("\n")
                
                else:
                    print("\nYou Need An Account To Continue\n")
                    break

        elif option == 'EX':
            print("***********************************")
            print("Thank You For Using Password Locker")
            print("***********************************")
            print("\n")
            break

        else:
            print("Wrong Option! Please Try Again.")
            print("\n")

if __name__ == '__main__':
    passlocker()