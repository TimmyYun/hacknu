from django.db import models
from django.db.models import DateTimeField

# Create your models here.

class DateTimeWithoutTZField(DateTimeField):
    def db_type(self, connection):
        return 'timestamp'

class Sale(models.Model):
    id = models.BigIntegerField(primary_key=True, blank=True)
    barcode = models.BigIntegerField(blank=True)
    quantity = models.IntegerField(default=1, blank=True)
    price = models.IntegerField(default=0, blank=True)
    saleTime = DateTimeWithoutTZField(auto_now_add=True, blank=True)
    
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
    supplyTime = DateTimeWithoutTZField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=["barcode", "supplyTime"]),
        ]
        db_table = "supply"
