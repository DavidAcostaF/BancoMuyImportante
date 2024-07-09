from django.db import models
from apps.card.models import Card

# Create your models here.


class Transaction(models.Model):
    TRANSFER = 'TR'
    WITHOUT_ACCOUNT = 'WA'
    TRANSACTION_TYPES = [
        (TRANSFER, 'Transfer'),
        (WITHOUT_ACCOUNT, 'Without Account'),
    ]
    
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=2, choices=TRANSACTION_TYPES)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    
    class Meta:
        abstract = True

class Transfer(Transaction):
    reference_number = models.CharField(max_length=50)
    destination_account = models.ForeignKey(Card, related_name='destination_account', on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        self.type = self.TRANSFER
        super().save(*args, **kwargs)

class WithoutAccount(Transaction):
    password = models.CharField(max_length=50)
    reference_number = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.type = self.WITHOUT_ACCOUNT
        super().save(*args, **kwargs)
