# store/models/payment.py
from django.db import models
from high_api_v1.models import BaseModel
from store.models import Order

class Payment(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=255)

    def __str__(self):
        return f"Payment {self.id} - Order: {self.order.id}, Amount: {self.amount}"
