class Bank:

    def __init__(self, balance: list[int]):

        self.balance = balance
        self.size = len(balance)
        
    def transfer(self, account1: int, account2: int, money: int) -> bool:

        account1-=1
        account2-=1

        
        if account1 < self.size and account2 < self.size:
            if self.balance[account1] >= money:

                self.balance[account1]-=money
                self.balance[account2]+=money
                
                return True

            else:
                return False
        else:
            return False
        

    def deposit(self, account: int, money: int) -> bool:

        if money <= 0:
            return True

        account-=1

        if account < self.size:
            self.balance[account] += money
            return True
        else:
            return False
        

    def withdraw(self, account: int, money: int) -> bool:

        if money <= 0:
            return True

        account-=1

        if account < self.size:

            bal = self.balance[account]
            
            if bal <= 0:
                return False
            
            elif bal - money < 0:
                return False

            else:
                self.balance[account]-=money
                return True

        else:
            return False
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
