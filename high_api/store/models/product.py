# models.py
from django.db import models
from high_api_v1.models import BaseModel
from store.models.category import Category

# Product model
class Product(BaseModel):
    name = models.CharField(max_length=255)
    price = models.BigIntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
