from django.db import models
from high_api_v1.models import BaseModel

# Category model
class Category(BaseModel):
    name = models.CharField(max_length=255)
    order = models.IntegerField()

    def __str__(self):
        return self.name