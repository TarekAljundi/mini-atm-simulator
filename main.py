# Functions


def menu():
    
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit",end="\n\n")
    


def check_balance():
    
    print(f"Your balance is {balance}",end="\n\n")


def deposit_money(balance):
    
    deposit=int(input("Enter amount to deposit: "))
    print("")
    
    new_balance = balance + deposit
    print(f"Deposit successful. New balance ={new_balance}",end="\n\n")
    
    return new_balance


 
def withdraw_money(balance):
    
        withdraw_amount=int(input("Enter amount to withdraw: "))
        print("")
        
        if withdraw_amount>balance:
           print("Insufficient funds!",end="\n\n")
           return balance
        else:
            new_balance= balance - withdraw_amount
            print(f"Withdrawal successful. New balance = {new_balance}",end="\n\n")
            
            return new_balance


def exit():
    print("Goodbye!",end="\n\n")


# Variables

balance=1000
atm_status=True


# Start of mini ATM

print("Welcome to the ATM")
print(f"Your balance is {balance}",end="\n\n")



while atm_status:
    
# Show Menu
    
    menu()
    
    # Try if the user input an invalid amount 
    
    try:
        
     # Ask for your  Choice
        user_choice= input("Choose an option: ")
        print("")
        
     # Verify choice
     
        if user_choice == "1":
            check_balance()
            
        elif user_choice == "2":
            balance = deposit_money(balance)
            
        elif user_choice == "3":
            balance = withdraw_money(balance)
            
        elif user_choice == "4":
            exit()
            atm_status = False
            
        else:
            print("Invalid choice. Please enter a valid option",end="\n\n")
    
            
    except ValueError:
        print("Invalid Input. Retry.",end="\n\n")    
