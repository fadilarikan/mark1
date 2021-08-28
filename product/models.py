from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    product_id = models.CharField(primary_key=True,max_length=100,verbose_name="Ürün No")
    miad = models.DateField(blank=True,verbose_name="Miad")
    purchase = models.BooleanField(default=False)
    purchase_date= models.DateField(blank=True,null=True,verbose_name="Satış Tarihi")
    stock = models.IntegerField(default=200,verbose_name="Stok Durumu")

    def __str__(self):
        return self.name
