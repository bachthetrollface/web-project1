from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, HttpRequest
from .models import Item, Category, ItemSpecification
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    category_list = Category.objects.order_by("name")
    context = {
        'category_list': category_list
    }
    return render(request, "home/index.html", context)


def about(request):
    return render(request, "home/about.html") # add about.html; maybe dont need

def log_in(request:HttpRequest):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("index") # return to current page instead of just home page
        else:
            # displays message
            return render(request, "home/login.html", {'message': "Invalid username and/or password"})
    else:
        if request.user.is_authenticated:
            return redirect("index") # return to current page
        else:
            return render(request, "home/login.html")

def log_out(request):
    logout(request)
    return redirect("index") # return to current page
    
def register(request:HttpRequest):
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']

        # check password confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "home/register.html", {'message': "Passwords must match."})

        # try if username is available
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        except:
            return render(request, "home/register.html", {'message': "Username already taken."})
        
        if request.user.is_authenticated:
            logout(request)
        login(request, user)
        return redirect("index")
    else:
        return render(request, "home/register.html")


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


def query(request):
    # action listener to update page as user types keywords?
    # query on Item table, returns records with keywords in their names
    return render(request, "home/query.html")


@login_required
def cart_index(request):
    # show items in cart of the current user
    # allows quantity update, item removal
    return render(request, "home/cart_index.html")


@login_required
def checkout(request):
    # lets user fill in information (see Purchase in models)
    # email, first name, last name is set default as info from user
    return render(request, "home/checkout.html")