from models.AccountHolder import AccountHolder
from mangers.AccountHolderManager import AccountHolderManager

acount_holder_manager = AccountHolderManager()


def mainMenu():
    print("Welcome to CodeBank" '\n' "Enter 0 to Quit" '\n' "Enter 1 to go to Account Holder Menu")


def show_sub_menu(option):
    if option == 0:
        print('Thank you for using CodeBank')
    elif option == 1:
        show_account_holder_menu()
        action = int(input())
        if action == 0:
            mainMenu()
        else:
            handle_account_holder_menu(action)


def show_account_holder_menu():
    print("Enter 1 to Register"'\n'"Enter 2 to update your details"'\n'"Enter 3 to change password"'\n'"Enter 4 to search"'\n'"Enter 5 to delete an account holder"'\n'"Enter 6 to list"'\n'"Enter 0 to go back")


def handle_account_holder_menu(action):
    if action == 1:
        email = str(input('Enter your email address: '))
        password = str(input('Enter Your password: '))
        confirm_password = str(input('Confirm your password: '))
        first_name = str(input(
            'Enter your first name'))
        last_name = str(input(
            'Enter your last name' '\t' 'if the last name is not given None will be used'))
        middle_name = str(input(
            'Enter your middle name' '\t' 'if the middle name is not given None will be used'))
        phone = str(input(
            'Enter your phone number' '\t' 'if phone number is not given None will be used'))
        holder = acount_holder_manager.create_account_holder(
            email=email, password=password, confirm_password=confirm_password, first_name=first_name, last_name=last_name, phone=phone, middle_name=middle_name)
        if holder is True:
            print(
                'Congrats Your account have been created' '\t' 'Your password is your first name')
        else:
            print('Password is incorrect')

    elif action == 2:
        email = str(input('Enter your email address: '))
        password = str(input('Enter Your password: '))
        holder = acount_holder_manager.login(email=email, password=password)
        if holder is False:
            print('Email or password incorrect')
        else:
            first_name = str(input(
                'Enter your first name'))
            last_name = str(input(
                'Enter your last name' '\t' 'if the last name is not given None will be used'))
            middle_name = str(input(
                'Enter your middle name' '\t' 'if the middle name is not given None will be used'))
            phone = str(input(
                'Enter your phone number' '\t' 'if phone number is not given None will be used'))
            new_holder = acount_holder_manager.update_account_holder(
                email=email, first_name=first_name, last_name=last_name, phone=phone, middle_name=middle_name)
            if new_holder is True:
                print('Update valid')
            else:
                print('Update invalid')

    elif action == 3:
        email = str(input('Enter your email address: '))
        new_password = str(input('Enter the new password: '))
        status = acount_holder_manager.change_password(
            email=email, new_password=new_password)
        if status is True:
            print('Password is valid')
        else:
            print('information invaid')

    elif action == 4:
        email = str(input('Enter your email address: '))
        holder = acount_holder_manager.search(email=email)
        if holder is False:
            print('Not Found')

    elif action == 5:
        email = str(input('Enter your email address: '))
        password = str(input('Enter Your password: '))
        holder = acount_holder_manager.login(email=email, password=password)
        if holder is False:
            print('password incorrect')
        else:
            status = acount_holder_manager.delete_account_holder(email=email)
            if status is True:
                print('Account Deleted')
            else:
                print('Account not deleted')

    elif action == 6:
        acount_holder_manager.list_account_holders()


show_sub_menu(1)


def main():
    flag = True
    while(flag):
        mainMenu()
        option = int(input())
        if(option == 0):
            flag = False
        else:
            show_sub_menu(option)


main()
