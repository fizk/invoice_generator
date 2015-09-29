from django.db import models
from django.utils import timezone

class Invoice(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=256, null=True)
    country = models.CharField(max_length=256, null=True)
    email = models.CharField(max_length=256, null=True)
    date = models.DateField(auto_now_add=False, null=True)
    currency = models.CharField(max_length=256, null=True)
    closed = models.BooleanField(default=False)
    success = models.BooleanField(default=False)

class Item(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='items')
    description = models.CharField(max_length=100)
    amount = models.IntegerField()

    class Meta:
        ordering = ['amount']

    def __unicode__(self):
        return '%s: %d' % (self.description, self.amount) #Used to print out the values of each item in the invoice_generator.


