from django.db import models

class Investor(models.Model):
    iban = models.CharField(max_length=34)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    joined_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Bill(models.Model):
    BILL_TYPES = [
        ('upfront_fees', 'Upfront Fees'),
        ('yearly_fees', 'Yearly Fees'),
    ]
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    bill_type = models.CharField(max_length=20, choices=BILL_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=255)
    due_date = models.DateField()


    def __str__(self):
        return self.name


class CapitalCall(models.Model):
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    bills = models.ManyToManyField(Bill)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('validated', 'Validated'),
        ('sent', 'Sent'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue'),
    ])
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.total_amount

