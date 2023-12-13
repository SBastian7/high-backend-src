from django.db import models
from django.contrib.auth.models import User
from high_api_v1.models import BaseModel
from store.models import Product

class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"Order {self.id}"
    

class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"OrderItem {self.id} - Product: {self.product.name}, Quantity: {self.quantity}"
