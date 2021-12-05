from user import User

def login_user(username, password):
    check_user =  User.verify_user(username, password)
    return check_user

def create_new_user(username, password):
    new_user = User(username, password)
    return new_user

def save_users(user):
    user.save_user()

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
            while True:
                if login:
                    print("\n")
                    print("**************************************************************")
                    print("Login Successful!! Welcome Back To Password Locker", username)
                    print("**************************************************************")
                    print("\n")
                    print("Dashboard Menu")
                    print("**************")
                    print("Please choose one of the following shortcodes to get continue:")
                    print("NC - Create A New Credential")
                    print("LD - Display Login Detials")
                    print("DS - Display Saved Credentials")
                    print("DC - Delete A Saved Credential")
                    print("DA - Delete Entire Account")
                    print("LO - Logout Application")
                    print("\n")
                    option = input("Your Choice: ").upper()
                    print("\n")

                    if option == 'NC':
                        pass

                    elif option == 'LD':
                        pass

                    elif option == 'DS':
                        pass

                    elif option == 'DC':
                        pass

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