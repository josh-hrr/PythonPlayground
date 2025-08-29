class Bank:

  def __init__(self, owner, initial_balance=0):
    self.owner = owner
    self.__balance = initial_balance

  @property
  def balance(self):
    return self.__balance
  
  @balance.setter
  def balance(self, amount):
    if amount < 0:
      raise ValueError("Amount must be positive")
    self.__balance += amount

  @classmethod
  def create_saving_account(cls, owner, initial_deposit):
    account = cls(owner, initial_deposit)
    return account

account = Bank("Josue", 100)
print(account.balance)

# showing property usage  
account.balance = 50
print(account.balance)

# showing second constructor usage
saving_account = Bank.create_saving_account("Alice", 500)
print(saving_account.balance)
print(saving_account.owner)
