class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self,n):
        self.balance += n

    def withdraw(self,n):
        if self.balance < n:
            print("余额不够。")
        else :
            self.balance -= n

    def get_balance(self):
        return self.balance

b = BankAccount()
b.deposit(100)
b.withdraw(500)    # 余额不足
print(b.get_balance())   # 还是 100，没扣成负数
b.withdraw(30)     # 正常取
print(b.get_balance())   # 70

