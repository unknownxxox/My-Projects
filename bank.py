# Users
Accounts = {"Ahmed": {"Balance": 100},"Mohamed": {"Balance": 250},"Abdallah": {"Balance": 300}}

# Login
name = input("Enter Your Account Name: ")

    
if name in Accounts:
    print(f"Welcome Back, {name}")

    print("Choose An Operation From The List:")
    print("1. Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")

    choice = input("Enter Your Operation Number: ")

    if choice == "1":
        print("Your Current Balance Is:", Accounts[name]["Balance"])    
        
        

    elif choice == "2":
        Amount = float(input("Enter Amount To Deposit: "))
        Accounts[name]["Balance"] += Amount
        print("Deposit Successful. New Balance Is:", Accounts[name]["Balance"])

    elif choice == "3":
        Amount = float(input("Enter Your Amount To Withdraw: "))
        if Amount <= Accounts[name]["Balance"]:
            Accounts[name]["Balance"] -= Amount
            print("Withdrawal Successful. New Balance Is:", Accounts[name]["Balance"])
        else:
            print("Insufficient Balance.")
            

    else:
        print("Invalid choice.")
else:
    print("Sorry User Not Found.")

    
