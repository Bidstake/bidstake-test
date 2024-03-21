from django.shortcuts import render

def index(request):    
    return render(request, "auctions/index.html",{
        # "a1": auctionlist.objects.filter(active_bool = True),
            })
