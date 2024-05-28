from django.contrib.auth import authenticate, login as auth_login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import *
from django.contrib.auth.decorators import login_required
from decimal import Decimal, InvalidOperation


def index(request):
    return render(request, 'auctions/index.html')

def profile(request):
    return render(request, 'auctions/profile.html')
def detail(request):
    return render(request, 'auctions/product-detail.html')
def products(request):
    return render(request, 'auctions/products.html')
def faq(request):
    return render(request, 'auctions/faq.html')
def contact(request):
    return render(request, 'auctions/contact.html')
def about(request):
    return render(request, 'auctions/about.html')
# login
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        phone = request.POST["phone"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })
        try:
            user = User.objects.create_user(username, phone, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        auth_login(request, user) 
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")



def create(request):
    return render(request, 'auctions/create.html')
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        starting_bid = request.POST.get('starting_bid')
        image = request.FILES.get('image')

        try:
            starting_bid_decimal = Decimal(starting_bid)
        except InvalidOperation:
            return render(request, 'auctions/create.html', {
                'error_message': "Invalid starting bid amount. Please enter a valid number."
            })

        if title and description and starting_bid:
            listing = Listing(
                title=title,
                description=description,
                starting_bid=starting_bid_decimal,
                current_bid=starting_bid_decimal,
                image=image,
                user=request.user
            )
            listing.save()
            return redirect('products')

    return render(request, 'auctions/create.html')
# def products(request):
#     listings = Listing.objects.all()

#     return render(request, 'auctions/products.html', {'listings': listings})
def products(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    # return render(request, 'auctions/products.html', {'listings': listings}
    return render(request, 'auctions/products.html', context)

@login_required
def bid(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    bids = Bid.objects.filter(listing=listing).order_by('-bid_time')

    if request.method == 'POST':
        bid_amount_str = request.POST.get('bid_amount')
        try:
            bid_amount = Decimal(bid_amount_str)
        except InvalidOperation:
            return render(request, 'auctions/bid.html', {
                'listing': listing,
                'bids': bids,
                'error_message': "Invalid bid amount. Please enter a valid number."
            })

        if bid_amount > listing.current_bid and bid_amount >= listing.starting_bid:
            # Update current bid amount for the listing
            listing.current_bid = bid_amount
            listing.save()

            # Create a new Bid instance
            bid = Bid(listing=listing, bidder=request.user, bid_amount=bid_amount)
            bid.save()

            # Redirect to the bid page for the same listing
            return redirect('bid', listing_id=listing.id)
        else:
            return render(request, 'auctions/bid.html', {
                'listing': listing,
                'bids': bids,
                'error_message': "Your bid must be higher than the current bid and at least the starting bid."
            })

    context = {
        'listing': listing,
        'bids': bids
    }
    return render(request, 'auctions/bid.html', context)