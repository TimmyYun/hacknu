from django.db import models

# Create your models here.

class Sale(models.Model):
    barcode = models.BigIntegerField()
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    sale_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=["barcode", "sale_time"]),
        ]
        db_table = "sale"


class Supply(models.Model):
    barcode = models.BigIntegerField()
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    supply_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=["barcode", "supply_time"]),
        ]
        db_table = "supply"
