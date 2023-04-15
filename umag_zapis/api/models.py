from django.db import models

# Create your models here.

class Sale(models.Model):
    id = models.BigIntegerField(primary_key=True, blank=True)
    barcode = models.BigIntegerField(blank=True)
    quantity = models.IntegerField(default=1, blank=True)
    price = models.IntegerField(default=0, blank=True)
    saleTime = models.DateTimeField(auto_now_add=True, blank=True)
    
    class Meta:
        indexes = [
            models.Index(fields=["barcode", "saleTime"]),
        ]
        db_table = "sale"


class Supply(models.Model):
    id = models.BigIntegerField(primary_key=True)
    barcode = models.BigIntegerField()
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    supplyTime = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=["barcode", "supplyTime"]),
        ]
        db_table = "supply"
