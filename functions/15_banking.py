
from random import randint

class Bank:
    def __init__(self) -> None:
        self.account = randint(100000,999999)
        self.full_name = input("Enter name = ")
        self.phonenumber = int(input("Enter phone number"))
        self.balance = 0


    def show_info(self):
        print(f"Account Number = {self.account}")
        print(f"Full Name = {self.full_name}")
        print(f"Balance = {self.balance}\n")


    def show_balance(self) -> None:
        print(f"Current Balance = {self.balance}")


    def withdraw(self)-> None:
        amount = int(input("Enter amount to withdraw ="))
        if amount>self.balance:
            print("In sufficient balance")
        else:
            # self.balance = self.balance - amount
            self.balance -= amount

    def deposit(self)-> None:
        amount = int(input("Enter amount to deposit = "))
        self.balance += amount


banks = []


def check_account_exists(acc_no :int):
    " to check account exists from a list of accounts"
    global banks
    for obj in banks:
        if obj.account == acc_no:
            return obj
    return None

    

while True:  # infinite  loop
    print("1. Create account ")
    print("2. Show all bank details")
    print("3. Deposit Amount")
    print("4. Withdraw Amount")
    print("5. Transfer Amount")
    print("6. Exit")
    choice = int(input("Enter choose = "))

    if choice==1:
        obj = Bank()
        banks.append(obj)
        print(banks)
    elif choice==2:
        if len(banks)==0:
            print("No accounts have been created yet")
        else:
            for account in banks:
                account.show_info()
    elif choice==3:
        if len(banks)==0:
            print("No accounts have been created yet")
        else:
            account_number = int(input("Enter account number to deposit"))
            for obj in banks:
                if obj.account == account_number:
                    obj.deposit()
                    break

    elif choice==4:
        if len(banks)==0:
            print("No accounts have been created yet")
        else:
            account_number = int(input("Enter account number to withdraw"))
            for obj in banks:
                if obj.account == account_number:
                    obj.withdraw()
                    break

    elif choice==5:
        from_acc_num = int(input("Enter account number from which you want to transfer")) 

        to_acc_num = int(input("Enter account number to which you want to transfer")) 
        from_acc_obj = check_account_exists(from_acc_num)
        to_acc_obj = check_account_exists(to_acc_num)
        if from_acc_obj!=None and to_acc_obj!=None:
            transfer_amount = int(input("Enter transfer amount"))
            if from_acc_obj.balance < transfer_amount:
                print("Insufficient Balance")
            else:
                from_acc_obj.balance -= transfer_amount
                to_acc_obj.balance += transfer_amount
        else:
            print("Account does not exist")

    elif choice==6:
        break
    else:
        print("Invalid Choice")



# x = Bank()
# banks.append(x)
# print(banks)

# y = Bank()
# banks.append(y)
# print(banks)

# banks[0].show_balance()
# banks[1].deposit()
# banks[1].show_balance()

# b1 = Bank()
# b2 = Bank()
# b1.show_balance()
# b1.deposit()
# b1.show_balance()
# b1.withdraw()
# b1.show_balance()