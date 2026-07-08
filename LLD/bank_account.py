class BankAccount:

    def __init__(self, acnumber, owner_name, balance=0):
        self.acnumber = acnumber
        self.owner_name = owner_name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance+= amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "false"
        
        else:
            self.balance -= amount
        
    def get_balance(self):
        return self.balance

user_account = BankAccount(acnumber="123213", owner_name="good")
