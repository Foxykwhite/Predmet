from django.db import models

# Create your models here.

# Учёт заказов в интернет-магазине

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    date_registered = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('completed', 'Completed'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')

    def __str__(self):
        return f"Order {self.id} - {self.user.name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Order {self.order.id})"