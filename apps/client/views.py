from django.shortcuts import render

# Create your views here.


"""
    def deposit(self, amount):
        self.balance += amount
        self.save()

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.save()
        else:
            raise ValueError("Insufficient balance")

    def transfer(self, amount, destination_account:'Client'):
        if self.balance >= amount:
            self.balance -= amount
            destination_account.deposit(amount)
            self.save()
        else:
            raise ValueError("Insufficient balance")
"""