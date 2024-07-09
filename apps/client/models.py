from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.middle_name}"

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