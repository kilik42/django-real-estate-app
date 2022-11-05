from django.shortcuts import render

# Create your views here.
from .models import Listing

#CRUD - CREATE, RETRIEVE, UPDATE AND DELETE, LIST(multiple records)

def listing_list(request):
    #orm object relational mapper
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, "listings.html", context)





