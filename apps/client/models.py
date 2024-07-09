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


