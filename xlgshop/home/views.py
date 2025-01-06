from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpRequest
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


def log_in(request:HttpRequest):
    if request.method == 'POST':
        username = request.POST['username']
        if len(username) == 0:
            return render(request, "home/login.html", {'message': "Hãy nhập tên đăng nhập!"})
        password = request.POST['password']
        if len(password) == 0:
            return render(request, "home/login.html", {'message': "Hãy nhập mật khẩu!"})
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("index") # return to current page instead of just home page
        else:
            # displays message
            return render(request, "home/login.html", {'message': "Tên đăng nhập hoặc mật khẩu không đúng."})
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
        if len(first_name) == 0:
            return render(request, "home/login.html", {'message': "Hãy nhập tên của bạn!"})
        last_name = request.POST['lastname']
        if len(last_name) == 0:
            return render(request, "home/login.html", {'message': "Hãy nhập họ của bạn!"})
        username = request.POST['username']
        if len(username) == 0:
            return render(request, "home/login.html", {'message': "Hãy nhập tên đăng nhập!"})
        email = request.POST['email']
        if len(email) == 0:
            return render(request, "home/login.html", {'message': "Hãy nhập email của bạn!"})

        # check password confirmation
        password = request.POST["password"]
        if len(password) == 0:
            return render(request, "home/login.html", {'message': "Hãy nhập mật khẩu!"})
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "home/register.html", {'message': "Mật khẩu không trùng khớp."})

        # try if username is available
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        except:
            return render(request, "home/register.html", 
                          {'message': "Tên đăng nhập này đã được sử dụng.\nHãy thử tên đăng nhập khác."})
        
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


def query(request:HttpRequest):
    # query on Item table, returns records with keywords in their names
    if request.method == "POST":
        context = dict()
        keyword = request.POST['keyword'].lower()
        items = Item.objects.all()
        results = []
        for item in items:
            if keyword in item.name.lower():
                results.append(item)
        if len(results) != 0:
            context['results'] = results
            context['message'] = f"Tìm thấy {len(results)} sản phẩm"
        else:
            context['message'] = "Không tìm thấy sản phẩm nào"
        return render(request, "home/query.html", context)
    else:
        context = {
            'message': "Nhập từ khoá để tìm kiếm"
        }
        return render(request, "home/query.html", context)
