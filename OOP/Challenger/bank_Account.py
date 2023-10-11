class MinimumBalanceError:
    pass

class Account:
    MINIMUM = 1000
    AccNumber = 1001

    def __init__(self, name, balance) -> None:
        if balance < self.MINIMUM:
            raise MinimumBalanceError('Account Cannot be Create')
        self.name = name
        self.balance = balance
        self.account_number = self.AccNumber
        self.AccNumber+=1
    
    def deposit(self, number):
        self.balance += number
    
    def withdraw(self, number):
        if self.balance - number < self.MINIMUM:
            raise MinimumBalanceError('Account cannot be withdraw')
        self.balance -= number

    def show_detail(self):
        print('Account number: ',self.AccNumber)
        print('Name: ',self.name)
        print('Balance: ',self.balance)

a1 = Account('Trung',2000)
a1.show_detail()
a1.deposit(1000)
a1.show_detail()
print("")

a2 = Account("Hoa", 950)
    