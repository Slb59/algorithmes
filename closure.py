class Account:
    def __init__(self, initial_amount):
        self.balance = initial_amount

    def salary(self, amount):
        def increment():
            self.balance += amount
            return self.balance
        return increment

    def invoice(self, amount):
        def decrement():
            if amount <= self.balance:
                self.balance -= amount
                return self.balance
            else:
                return "You have to work more!"
        return decrement


# Create an instance of Account
account = Account(1000)

# define salary and invoice functions
salary = account.salary(500)
invoice = account.invoice(400)

# Use the deposit and withdraw functions
print(salary())    # Output: 1500
print(invoice())   # Output: 1100
print(invoice())   # Output: 700
print(invoice())   # Output: 300
print(invoice())   # Output: You have to work more!