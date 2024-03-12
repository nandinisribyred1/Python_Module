username = ['nandu', 'chandana', 'santu', 'rohitha']
password = ['nandu04', 'chandana18', 'santu03', 'rohitha23']
pincode = [2131, 2135, 2023, 2456]
acc_bal = [240450, 20000, 400000, 100000]

def pas_change(new_pass, con_pass):
    index = username.index(user)
    if new_pass == con_pass:
        print("Password changed successfully.")
        password[index] = new_pass
        return

def atm():
    index = username.index(user)
    print("Enter your password:")
    p = input()
    if p != password[index]:
        print("Incorrect Password, 2 more attempts")
        p = input()
        if p != password[index]:
            print("Incorrect Password, 1 more attempt")
            p = input()
            if p != password[index]:
                print("Access Denied, Account Blocked")
                return
    print("1.Withdrawl")
    print("2.Deposit")
    print("3.Account Balance")
    print("4.Change Password")
    while True:
        print("Enter your choice:")
        choice = int(input())
        if choice in [1, 2, 3, 4]:
            break
        else:
            print("Invalid choice. Please choose from the given options.")
            
    #--------------------------WITHDRAWL----------------------------------        
    if choice == 1:
        am = int(input("Enter amount to withdraw: "))
        pin = int(input("Enter pincode:"))
        if pin != pincode[index]:
            print("Invalid PIN")
            print("END")
        else:        
            if am > acc_bal[index]:
                print("Insufficient balance")
                return
            acc_bal[index] -= am
            print("Withdrawal successful.")
            print("Do you want to display balance? (y/n)")
            na = input()
            if na == 'y':
                print("Your available balance is:", acc_bal[index])
                print("Thank You for banking with us")
            else:
                print("Thank You for banking with us")    
    #--------------------------DEPOSIT----------------------------------            
    elif choice == 2:
        am = int(input("Enter amount to deposit: "))
        pin = int(input("Enter pincode:"))
        if pin != pincode[index]:
            print("Invalid PIN")
            print("END")
        else:        
            acc_bal[index] += am
            print("Deposit successful.")
            print("Do you want to display balance? (y/n)")
            na = input()
            if na == 'y':
                print("Your available balance is:", acc_bal[index])
                print("Thank You for banking with us")
            else:
                print("Thank You for banking with us")
    #--------------------------ACCOUNT BALANCE----------------------------------            
    elif choice == 3:
        pin = int(input("Enter pincode:"))
        if pin != pincode[index]:
            print("Invalid PIN")
            print("END")
        else:        
            print("Your account balance is:", acc_bal[index])
    #---------------------------CHANGE PASSWORD----------------------------------        
    elif choice == 4:
        new = input("Enter new password: ")
        if new == password[index]:
            print("New and Old password cannot be same")
            return
        else:
            while True:
                new1 = input("Enter new password: ")
                con = input("Enter the password again:")
                if new1 == con:
                    password[index] = new1
                    print("Password changed successfully.")
                    break
                else:
                    print("Re-enter the password again...")


user=input("Enter username:")
if user not in username:
    print("Invalid Username")
    print("END")
else:
    atm()
    print("END")                    