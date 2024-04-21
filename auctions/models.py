from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    pass
from django.db import models

class auctionlist(models.Model):
    user = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    image_url = models.JSONField()
    active_bool = models.BooleanField(default=True)  # Add default value

    def __str__(self):
        return self.title

