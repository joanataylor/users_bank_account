class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_deposit(self, amount):
      self.account.deposit(amount)
      return self

    def make_withdrawal(self, amount):
      self.account.withdraw(amount)
      return self

    def display_user_balance(self):
      print(f"Name is: {self.name}")
      print(f"Email is: {self.email}")
      self.account.display_account_info()
      # print(self.account.balance)
      return self


class BankAccount:
  all_accounts = []
  def __init__(self, int_rate, balance):
    self.int_rate = int_rate
    self.balance = balance
  
  def deposit(self, amount):
    self.balance += amount
    print(f"After the deposit was made this is the current balance: ${self.balance}")
    return self

#decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
  def withdraw(self, amount):
    if amount < self.balance:
        self.balance -= amount
    else:
        print("Insufficient funds: Charging a $5 fee")
        self.balance -= 5
    print(f"After the withdraw the updated balance is: ${self.balance}")
    return self

#print to the console: eg. "Balance: $100"
  def display_account_info(self):
    print(f"Interest Rate is: {self.int_rate}%")
    print(f"Balance is: ${self.balance}")
    return self

#increases the account balance by the current balance * the interest rate (as long as the balance is positive)
  def yield_interest(self):
    self.balance *= (1+ self.int_rate)
    return self


user_joana = User("Joana", "joana_grave@gmail.com")
# user_Poppi = User("Poppi", "poppi.moore@gmail.com")
# user_joana.display_user_balance()
user_joana.make_deposit(333).make_withdrawal(29).display_user_balance()