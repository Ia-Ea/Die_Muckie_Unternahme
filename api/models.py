from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    short_description = models.TextField()
    product_description = models.TextField()
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
   

    def __str__(self):
        return self.name
    
class Stock(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='stocks'
    )
    quantity = models.IntegerField()

    def __str__(self):
        return f"Stock for {self.product.name}: {self.quantity}"