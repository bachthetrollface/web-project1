from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse
from .models import Item, Category, ItemSpecification
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def index(request):
    category_list = Category.objects.order_by("name")
    context = {
        'category_list': category_list
    }
    return render(request, "home/index.html", context)


def about(request):
    return render(request, "home/about.html", dict()) # add about.html


def log_in(request):
    pass

def log_out(request):
    logout(request)
    return redirect("index")
    
def register(request):
    pass


def categories(request, category_name):
    category_name = " ".join(category_name.split("%20"))
    try:
        item_list = get_list_or_404(Item, category=get_object_or_404(Category, name=category_name))
    except:
        item_list = None
    context = {
        'category': category_name,
        'item_list': item_list
    }
    return render(request, "home/categories.html", context)


def details(request, item_id):
    """
    update view as user selects size or colors,
    query to get unique values of each field,
    as a field is selected, re-query to get available unique values of remaining field
    """
    try:
        item = get_object_or_404(Item, id=item_id)
    except:
        item = None
    if item is not None:
        try:
            available_specs = get_list_or_404(ItemSpecification, item=item)
        except:
            available_specs = None
    else:
        available_specs = None
    context = {
        'item': item,
        'available_specs': available_specs
    }
    return render(request, "home/details.html", context)


def cart_index(request):
    return render(request, "home/cart_index.html", dict())