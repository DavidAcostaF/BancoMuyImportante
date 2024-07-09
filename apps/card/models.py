from django.db import models
from apps.client.models import Client

class Card(models.Model):
    CARD_TYPE_CHOICES = [
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    ]
    
    number = models.CharField(max_length=20, unique=True)
    opening_date = models.DateField()
    status = models.CharField(max_length=20)
    client = models.ForeignKey(Client, related_name='cards', on_delete=models.CASCADE)
    cardholder_name = models.CharField(max_length=100)
    expiration_date = models.DateField()
    cvv = models.CharField(max_length=4)
    card_type = models.CharField(max_length=10, choices=CARD_TYPE_CHOICES)

    def __str__(self):
        return f"{self.number} - {self.cardholder_name}"
