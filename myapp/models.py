from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Transaction {self.id} by {self.customer.name}'
