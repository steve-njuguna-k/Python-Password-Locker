from user import User

def login(username, password):
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
            pass

        elif option == 'EX':
            pass

        else:
            print("Wrong Option! Please Try Again.")

if __name__ == '__main__':
    passlocker()