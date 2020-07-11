from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    listings =Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 2)
    page_number = request.GET.get('page')
    paged_listings = paginator.get_page(page_number)
    
    context ={
        'listings':paged_listings
    }

    return render(request, "listings/listings.html", context)
def listing(request, listing_id):
    listing= get_object_or_404(Listing, pk=listing_id)
    context={
        'listing':listing    }
    return render(request, "listings/listing.html", context)
def search(request):
    return render(request, "listings/search.html")        


# Create your views here.
