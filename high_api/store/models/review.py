# store/models/review.py
from django.db import models
from django.contrib.auth.models import User
from high_api_v1.models import BaseModel
from store.models import Product

class Review(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.id} - Product: {self.product.name}, User: {self.user.username}, Rating: {self.rating}"
