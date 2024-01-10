class BankAccount:
    def __init__(self,account_holder_name,account_number,balance):
        self.account_holder_name=account_holder_name
        self.account_number=account_number
        self.balance=balance

    def deposit(self,amount):
            self.balance+=amount
            print(f'Rupees {amount}/- credited to A/c.{self.account_number}.')

    def withdraw(self,amount):
            if(amount<self.balance):
                self.balance-=amount
                print(f'Rupees {amount}/- debited from A/c.{self.account_number}.')
            elif(amount==self.balance):
                print("Minimum balance is needed in your account,Please try withdrawing a smaller amount.")
            else:
                print("Insufficient funds!!!")

    def display_current_balance(self):
        print(f'Current balance on A/c.{self.account_number} is {self.balance}')

    def get_account_holder_details(self):
        print(f'Account Holder Name: {self.account_holder_name},')
        print(f'Account Number: {self.account_number}.')

account1=BankAccount("ABC",98564345231,10000)
account2=BankAccount("DEF",98664345232,5000)
account3=BankAccount("EHI",98764345233,1000)
account4=BankAccount("XYZ",98864345234,85000)

print("**********Account Holders list and Details**********")
account1.get_account_holder_details()
account2.get_account_holder_details()
account3.get_account_holder_details()
account4.get_account_holder_details()

print("**********TRANSACTION HISTORY OF ACCOUNT HOLDERS**********")
account2.deposit(20000)
account4.withdraw(5000)
account3.deposit(9000)
account3.withdraw(10000)
account4.display_current_balance()


