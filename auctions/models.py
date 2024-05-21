from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='listing_images/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
# class auctionlist(models.Model):
#     user = models.CharField(max_length=64)
#     title = models.CharField(max_length=64)
#     desc = models.TextField()           #CharField cannot be left without giving a max_length, Textfield can
#     starting_bid = models.IntegerField()        
#     image_url = models.CharField(max_length=228, default = None, blank = True, null = True)
#     created_at = models.DateTimeField(default=timezone.now)
#     active_bool = models.BooleanField(default = True)

    def __str__(self):
        return self.title
