from django.shortcuts import render

# Create your views here.
from .models import Listing
from .forms import ListingForm

#CRUD - CREATE, RETRIEVE, UPDATE AND DELETE, LIST(multiple records)

def listing_list(request):
    #orm object relational mapper
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, "listings.html", context)


def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {
        "listing": listing
    }
    return render(request, "listing.html", context)



def listing_create(request):
    form = ListingForm()
    context = {
        "form":form
    }
    return render(request, "listing_create.html", context)

