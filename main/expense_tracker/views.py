from django.shortcuts import render, redirect
from .models import Data
from django.db.models import Sum
from django.utils.text import slugify
from datetime import datetime, date, timedelta
from .forms import NewUserForm
from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib import messages



today = datetime.now()
auto_time = today.strftime("%X")
auto_date = today.strftime("%Y-%m-%d")

def index_view(response):
    se_month = today.strftime("%b")
    se_year = today.year

    if response.POST:
        se_year = response.POST['sse_year']
        se_month = response.POST['sse_month']

    list_data = Data.objects.filter(year=se_year, month=se_month)
    data_dict = {}

    data_dict.setdefault("category_wise", {})
    # category wise total
    categories = ["Meal", "Shopping", "Vehicle", "Grocery", "Utility", "Online Shopping", "Gain", "Others"]
    for cat in categories:
        scrubed_cat = slugify(cat).replace('-', '_')
        data_dict["category_wise"].setdefault(scrubed_cat, 0)
        amount = Data.objects.filter(year=se_year, month=se_month, category=cat).aggregate(Sum('amount'))['amount__sum']
        if amount: 
            data_dict["category_wise"][scrubed_cat] = int(amount)
        else: 
            data_dict["category_wise"][scrubed_cat] = 0


    # monthly total
    months = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}

    data_dict.setdefault("monthly_total", {})
    for month in list(months.keys()):
        data_dict["monthly_total"].setdefault(month, 0)
        amount = Data.objects.filter(year=se_year, month=month).aggregate(Sum('amount'))["amount__sum"]
        if amount:
            data_dict["monthly_total"][month] = int(amount)
        else: 
            data_dict["monthly_total"][month] = 0


    yearly_expense = Data.objects.filter(year=se_year).aggregate(Sum('amount'))['amount__sum']
    monthly_expense = data_dict["monthly_total"].get(se_month)

    current_date = datetime(int(se_year), months[se_month], 1)
    previous_month = current_date - timedelta(days=current_date.day)

    if se_month == "Jan":
        se_year =  int(previous_month.year)

    past_expense = Data.objects.filter(
        year=se_year, 
        month=previous_month.strftime("%b")
    ).aggregate(Sum('amount'))["amount__sum"]

    gained_this_month = (
        float(past_expense if past_expense else 0.0) - 
        float(monthly_expense if monthly_expense else 0.0)
    )

    context = {
        "list_data" : list_data,
        "amounts": list(data_dict.get("category_wise").values()),
        "monthly_total": list(data_dict.get("monthly_total").values()),
        'se_option_year': se_year,
        'se_option_month': se_month,
        'total_year_expense': yearly_expense,
        'monthly_expense': monthly_expense,
        'gained_this_month' : gained_this_month,
    }
    return render(response, 'main/index.html', context)


def add_list(response):
    if response.POST:
        name = response.POST['add_name']
        category = response.POST["add_category"]
        amount = response.POST['add_amount']
        note = response.POST["add_note"]
        year = response.POST['add_year']
        month = response.POST["add_month"]

        db = Data()
        db.name = name
        db.category = category
        db.amount = amount
        db.note = note
        db.year = year
        db.month = month
        db.dateandtime = auto_date
        db.time = auto_time
        db.save()
    return render(response, 'main/add.html', {})


def list_view(response):
    if response.POST:
        se_year = response.POST['sse_year']
        se_month = response.POST['sse_month']
    else:
        se_month = today.strftime("%b")
        se_year = today.year
    list_data = Data.objects.filter(year= se_year, month= se_month)
    p = {
        'list_data': list_data,
        'se_year': se_year,
        'se_month': se_month,
    }
    return render(response, 'main/list.html', p)


def del_list(response, pk):
    item = Data.objects.get(id=pk)
    item.delete()
    return redirect('/list')


def signup_view(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)

            login(request, user)
            return HttpResponseRedirect("/index")

    else:
        form = NewUserForm()
    return render(request, 'main/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/index')
        else:
            messages.error(request, 'Invalid login credentials')

    return render(request, 'main/login.html')
