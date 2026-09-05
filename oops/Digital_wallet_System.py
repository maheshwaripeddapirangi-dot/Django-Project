class DigitalWallet:
    company_name="PayFlow"
    max_wallet_limit=100000

    def __init__(self,user_name,balance):
        self.user_name=user_name
        self.balance=balance
        self.transaction_history=[]
    
    def add_money(self,amount):

        # Check valid amount
        if not DigitalWallet.is_valid_amount(amount):
            print(" Invalid amount! Deposit amount must be greater than 0.")
            return

        # check wallet limt
        if self.balance+amount>DigitalWallet.max_wallet_limit:
            print("Wallet limit exeeded!")
            return
        
        self.balance+=amount
        self.transaction_history.append(f"Deposited {amount}")
        print(f"{amount} deposited successfully into {self.user_name}'s wallet.")


    def pay(self, amount):
        if not DigitalWallet.is_valid_amount(amount):
            print("Invalid amount! Payment amount must be greater than 0.")
            return

        if amount > 10000:
            print("Transaction above RS.10,000 is not allowed.")
            return

        final_amount = DigitalWallet.apply_transaction_fee(amount)

        if final_amount > self.balance:
           print(f"{self.user_name} has insufficient balance.")
           return

        self.balance -= final_amount
        self.transaction_history.append(
           f"Paid RS.{amount} (After 2% fee: RS.{final_amount:.2f})"
        )
        print(f"Payment successful.")
        print(f"Amount Paid : RS.{amount}")
        print(f"Amount Deducted (after fee): RS.{final_amount:.2f}")

    def check_balance(self):
        return self.balance
    
    def show_transaction_history(self):
        print(f"\n Transaction History of {self.user_name}")
        if len(self.transaction_history)==0:
            print("No transactions yet.")
        else:
            for transaction in self.transaction_history:
                print(transaction)
    
    @classmethod
    def change_company_name(cls,new_name):
        cls.company_name=new_name
        print(f"Company name changed to {cls.company_name}")

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

    @staticmethod
    def apply_transaction_fee(amount):
        return amount * 1.02
    
    def __str__(self):
        return (f"User:{self.user_name}\n"
                f"Balance: {self.balance:.2f}\n"
                f"Company:{DigitalWallet.company_name}")
    


s1 = DigitalWallet("Maheshwari", 50000)
s2 = DigitalWallet("Hony", 10000)

print(s1)
print()

print(s2)
print()

# Deposit
s1.add_money(10000)
print()

# Payment
s1.pay(5000)
print()

# Invalid deposit
s2.add_money(-500)
print()

# Invalid payment
s2.pay(15000)
print()

# Valid payment
s2.pay(3000)
print()

# Check Balance
print(f"{s1.user_name} Balance: RS.{s1.check_balance():.2f}")
print(f"{s2.user_name} Balance: RS.{s2.check_balance():.2f}")
print()

# Show transaction history
s1.show_transaction_history()
print()

s2.show_transaction_history()
print()

# Change company name
DigitalWallet.change_company_name("PayFlow India")
print()

print(s1)
print()
print(s2)