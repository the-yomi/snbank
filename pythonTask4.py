import random
import os
status = True
while status:
    choice_action = input("Staff Login \nClose App").lower()
    if choice_action == "staff login":
        username = input("enter username").lower()
        password = input("enter password").lower()
        staff_file = open("staff.txt","r+")        
        for info in staff_file.readlines():
            staff_details = info.split(",")
            username1 = staff_details[1]
            password1 = staff_details[3]

            if username == username1 and password == password1:     
                user_session_file = open("user_session.txt", "a")
                user_session_file.write("User is active")
                
                print("Log in sucessful!")
                staff_file.close()
                action_status = True
                while action_status: 
                    action_taken = input('''Use the designated number to indicate your choice of action:
        1. Create New Bank Account
        2. Check Account Balance
        3. Logout''')
                    if action_taken == "1":
               
                        print("please provide the following details")
                        account_name = input("Account Name").lower()
                        opening_balance = input("Opening Balance in Figures")
                        account_type = input("Account Type: Savings or Current").lower()
                        account_email = input("Account Email").lower()
                        account_number = "". join(map(str,[random.randrange(1, 9)for i in range (10)]))
                        customer_file = open("customer.txt", "r+")
                        customer_file.write("Account Name: %s \n" %account_name)
                        customer_file.write("Account Number: %s \n" %account_number)
                        customer_file.write("Opening Balance: %s \n" %opening_balance)
                        customer_file.write("Account Type: %s \n" %account_type)
                        customer_file.write("Account Email: %s " %account_email)
                        customer_file.close()
                        
                        print("Here is your account number ", account_number)
                
                    elif action_taken == "2":              
                        requested_acct_no = int(input("Enter your 10 digit account number"))
                        requested_acct_no == account_number
                        customer_file = open("customer.txt", "r")
                        print(customer_file.read())
                        customer_file.close()
                    
                    elif action_taken == "3":
                        print("You have been logged out")
                        user_session_file.close()
                        os.remove("user_session.txt")
                        action_status = False
                    else:
                        action_taken = input("please enter a valid option")
            else:
                print("Wrong username or password.Try again")
                username = input("enter username")
                password = input("enter password")
    
    elif choice_action == "close app":
        action_status = False
        status = False
    else:
        print("invalid action")

     