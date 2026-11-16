#Class
class SavingsAccount:
    #constructor function
    def __init__(self, account_id:int, balance:float, 
                 previous_balance:float, annual_interest_rate:float):
        self.account_id = account_id
        self.balance = balance
        self.previous_balance = previous_balance
        self.annual_interest_rate = annual_interest_rate

    #setters
    def set_interest_rate(self, updated_interest_rate):
        self.annual_interest_rate = updated_interest_rate

    def withdraw(self, amount:float) -> None:
            if amount > self.balance:
                print("Insufficient Balance")
            else:
                self.balance -= amount

    def deposit(self, amount:float) -> None:
        self.balance += amount


    #getters
    def get_monthly_interest_rate(self):
        return self.annual_interest_rate / 12 / 100

    def get_monthly_interest(self):
        return self.balance * self.get_monthly_interest_rate()

    def get_balance_change_percent(self): #% change
        return (self.balance - self.previous_balance) / self.previous_balance * 100
    
    def withdraw(self, amount:float) -> None:
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount



def cq() -> None:
    account = SavingsAccount(1122, 20_000.00, 18_500.00, 4.5)
    account.withdraw(2_500.0)
    account.deposit(3_000.0)
    print('Account ID: ', account.account_id)
    print('Current Balance: ', account.balance)
    print('Mounthly Interest Rate: ', account.get_monthly_interest_rate() * 100)
    print('Monthly Interest: ', account.get_monthly_interest())
    print('Percentage Change: ', account.get_balance_change_percent())

if __name__ == "__main__":
    cq()