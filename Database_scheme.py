from django.db import models
from django.utils import timezone

class ProductTransaction(models.Model):
    # Core Transaction Fields
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    image = models.URLField(null=True, blank=True)
    
    # Transaction Status Fields
    sold = models.BooleanField(default=False)
    dateOfSale = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'product_transactions'
        indexes = [
            models.Index(fields=['category']),
            models.Index(fields=['price']),
            models.Index(fields=['dateOfSale'])
        ]

    def _str_(self):
        return f"{self.title} - ${self.price}"