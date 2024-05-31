from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    pass

# class Listing(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
#     current_bid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     image = models.ImageField(upload_to='listing_images/', blank=True, null=True)
#     created_at = models.DateTimeField(default=timezone.now)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title

# class Bid(models.Model):
#     listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
#     bidder = models.ForeignKey(User, on_delete=models.CASCADE)
#     bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     bid_time = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return f"{self.bidder.username} - {self.bid_amount}"


class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='listing_images/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bid_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.bidder.username} - {self.bid_amount}"

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Message from {self.sender.username} to {self.receiver.username}"