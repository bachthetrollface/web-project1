from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Item

# Create your views here.
def index(request):
    latest_item_list = Item.objects.order_by("add_date")[:5]
    context = {
        'latest_item_list': latest_item_list
    }
    return render(request, "home/index.html", context)

def details(request, item_id):
    item = get_object_or_404(Item, item_id=item_id)
    return HttpResponse(f"Item: {item.item_name}; type: {item.item_type}; size: {item.size}; ID: {item.item_id}")