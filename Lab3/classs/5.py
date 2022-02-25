class bank_account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, quantity):
        self.balance += quantity

    def wwithdraw(self, money):
        if (self.balance / 10) >= money:
            self.balance -= money
            return f"You have withdrawed {money} tg"
        return "can't withdraw your funds"


s = int(input())
Bank = bank_account("Didar", s)
Bank.deposit(s / 10)
m = int(input())
print(Bank.wwithdraw(m))