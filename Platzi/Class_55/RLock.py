'''

A **deadlock** occurs when two or more threads block each other by waiting for a resource that is being used by another thread. To avoid this, we can use `RLock` instead of `Lock`.
if we use Lock instead, the process runs into a deadlock because the same thread is trying to acquire the lock it already holds.

'''
import threading

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.RLock()  # reentrant lock

    def transfer(self, other_account, amount):
        # This acquires self.lock
        with self.lock:
            print(f"Transferring {amount} from {self} to {other_account}")
            self.withdraw(amount)           # calls another method that ALSO acquires self.lock
            other_account.deposit(amount)   # acquires other_account.lock

    def withdraw(self, amount):
        with self.lock:  # same lock as in transfer
            self.balance -= amount

    def deposit(self, amount):
        with self.lock:
            self.balance += amount

    def __repr__(self):
        return f"<BankAccount balance={self.balance}>"

# Create two accounts
account1 = BankAccount(500)
account2 = BankAccount(300)

# Create threads that transfer between accounts
thread1 = threading.Thread(target=account1.transfer, args=(account2, 200))
thread2 = threading.Thread(target=account2.transfer, args=(account1, 100))

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(f"Account1 balance: {account1.balance}")
print(f"Account2 balance: {account2.balance}")
