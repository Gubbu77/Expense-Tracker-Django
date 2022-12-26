from django.shortcuts import render, redirect
from .models import Data
from datetime import datetime

# decimal context
from decimal import Decimal
from bson import Decimal128
import string
from django.db.models import Sum

# Create your views here.
today = datetime.now()
auto_time = today.strftime("%X")
auto_date =today.strftime("%Y-%m-%d")

def index_view(response):
    if response.POST:
        se_year = response.POST['sse_year']
        se_month = response.POST['sse_month']
    else:
        se_month = today.strftime("%b")
        se_year = today.year


    list_data = Data.objects.filter(year= se_year, month= se_month)

    # meal data
    meal_amt = Data.objects.filter(year= se_year, month= se_month, category = 'Meal').aggregate(Sum('amount'))['amount__sum']
    if meal_amt == None:
        meal_amt = 0
    # meal_amt = 0
    # for i in meal_data:
    #     id = i.id
    #     m_amount_data = Data.objects.get(id = id)
    #     meal_amt += m_amount_data.amount

    # Shopping data
    shop_amt = Data.objects.filter(year= se_year, month= se_month, category = 'Shopping').aggregate(Sum('amount'))['amount__sum']
    if shop_amt == None:
        shop_amt = 0

    # Vehicle data
    veh_amt = Data.objects.filter(year= se_year, month= se_month, category = 'Vehicle').aggregate(Sum('amount'))['amount__sum']
    if veh_amt == None:
        veh_amt = 0

    # Grocery data
    gro_amt = Data.objects.filter(year= se_year, month= se_month, category = 'Grocery').aggregate(Sum('amount'))['amount__sum']
    if gro_amt == None:
        gro_amt = 0
        
    # utility data
    util_amt = Data.objects.filter(year= se_year, month= se_month, category = 'Utility').aggregate(Sum('amount'))['amount__sum']
    if util_amt == None:
        util_amt = 0

    # Online shopping data
    os_amt = Data.objects.filter(year= se_year, month= se_month, category = 'Online Shopping').aggregate(Sum('amount'))['amount__sum']
    if os_amt == None:
        os_amt = 0

    # gain data
    gain_amt = Data.objects.filter(year= se_year, month= se_month, category = 'Gain').aggregate(Sum('amount'))['amount__sum']
    if gain_amt == None:
        gain_amt = 0

    # others data
    oth_amt = Data.objects.filter(year= se_year, month= se_month, category = 'Others').aggregate(Sum('amount'))['amount__sum']
    if oth_amt == None:
        oth_amt = 0

    # monthly total Aug////////////////////////////////////////////////////////
    data_of_year = Data.objects.filter(year= se_year)
    dec_total_amt = 0
    for i in data_of_year:
        if i.month == "Dec":
            id = i.id
            dec_amt = Data.objects.get(id = id)
            dec_total_amt += dec_amt.amount

    # monthly total Aug
    jan_total_amt = 0
    for i in data_of_year:
        if i.month == "Jan":
            id = i.id
            jan_amt = Data.objects.get(id = id)
            jan_total_amt += jan_amt.amount
    # monthly total feb
    feb_total_amt = 0
    for i in data_of_year:
        if i.month == "Feb":
            id = i.id
            feb_amt = Data.objects.get(id = id)
            feb_total_amt += feb_amt.amount

    # monthly total mar
    mar_total_amt = 0
    for i in data_of_year:
        if i.month == "Mar":
            id = i.id
            mar_amt = Data.objects.get(id = id)
            mar_total_amt += mar_amt.amount

    # monthly total apr
    apr_total_amt = 0
    for i in data_of_year:
        if i.month == "Apr":
            id = i.id
            apr_amt = Data.objects.get(id = id)
            apr_total_amt += apr_amt.amount

    # monthly total may
    may_total_amt = 0
    for i in data_of_year:
        if i.month == "May":
            id = i.id
            may_amt = Data.objects.get(id = id)
            may_total_amt += may_amt.amount

    # monthly total jun
    jun_total_amt = 0
    for i in data_of_year:
        if i.month == "Jun":
            id = i.id
            jun_amt = Data.objects.get(id = id)
            jun_total_amt += jun_amt.amount

    # monthly total july
    jul_total_amt = 0
    for i in data_of_year:
        if i.month == "July":
            id = i.id
            jul_amt = Data.objects.get(id = id)
            jul_total_amt += jul_amt.amount

    # monthly total aug
    aug_total_amt = 0
    for i in data_of_year:
        if i.month == "Aug":
            id = i.id
            aug_amt = Data.objects.get(id = id)
            aug_total_amt += aug_amt.amount

    # monthly total sep
    sep_total_amt = 0
    for i in data_of_year:
        if i.month == "Sep":
            id = i.id
            sep_amt = Data.objects.get(id = id)
            sep_total_amt += sep_amt.amount

    # monthly total oct
    oct_total_amt = 0
    for i in data_of_year:
        if i.month == "Oct":
            id = i.id
            oct_amt = Data.objects.get(id = id)
            oct_total_amt += oct_amt.amount

    # monthly total nov
    nov_total_amt = 0
    for i in data_of_year:
        if i.month == "Nov":
            id = i.id
            nov_amt = Data.objects.get(id = id)
            nov_total_amt += nov_amt.amount          

    total_year_expense = (
        jan_total_amt + 
        feb_total_amt +  
        mar_total_amt + 
        apr_total_amt + 
        may_total_amt +
        jun_total_amt +
        jul_total_amt +
        aug_total_amt +
        sep_total_amt +
        oct_total_amt +
        nov_total_amt +
        dec_total_amt )

    # monthly_expense :
    monthly_expense = Data.objects.filter(year= se_year, month= se_month).aggregate(Sum('amount'))['amount__sum']

    # gained this month :
    if se_month == "Jan":
        gained_this_month = 0
    if se_month == "Feb":
        gained_this_month = jan_total_amt - feb_total_amt
    if se_month == "Mar":
        gained_this_month = feb_total_amt - mar_total_amt
    if se_month == "Apr":
        gained_this_month = mar_total_amt - apr_total_amt
    if se_month == "May":
        gained_this_month = apr_total_amt - may_total_amt
    if se_month == "Jun":
        gained_this_month = may_total_amt - jun_total_amt
    if se_month == "Jul":
        gained_this_month = jun_total_amt - jul_total_amt
    if se_month == "Aug":
        gained_this_month = jul_total_amt - aug_total_amt
    if se_month == "Sep":
        gained_this_month = aug_total_amt - sep_total_amt
    if se_month == "Oct":
        gained_this_month = sep_total_amt - oct_total_amt
    if se_month == "Nov":
        gained_this_month = oct_total_amt - nov_total_amt
    if se_month == "Dec":
        gained_this_month = nov_total_amt - dec_total_amt
    
    

    p = {
        "list_data" : list_data,
        "meal_amt" : meal_amt,
        "shop_amt" : shop_amt,
        "veh_amt" : veh_amt,
        "gro_amt" : gro_amt,
        "util_amt" : util_amt,
        "os_amt" : os_amt,
        "gain_amt" : gain_amt,
        "oth_amt" : oth_amt,

        # monthly expense
        "dec_total_amt" : dec_total_amt,
        "jan_total_amt" : jan_total_amt,
        "feb_total_amt" : feb_total_amt,
        "mar_total_amt" : mar_total_amt,
        "apr_total_amt" : apr_total_amt,
        "may_total_amt" : may_total_amt,
        "jun_total_amt" : jun_total_amt,
        "jul_total_amt" : jul_total_amt,
        "aug_total_amt" : aug_total_amt,
        "sep_total_amt" : sep_total_amt,
        "oct_total_amt" : oct_total_amt,
        "nov_total_amt" : nov_total_amt,

        # year and month
        'se_option_year': se_year,
        'se_option_month': se_month,

        # total yearly and monthly expense
        'total_year_expense': total_year_expense,
        'monthly_expense': monthly_expense,

        # total gained
        'gained_this_month' : gained_this_month,

    }


    return render(response, 'main/index.html', p)

def add_list(response):
    if response.POST:
        name = response.POST['add_name']
        category = response.POST["add_category"]
        amount = response.POST['add_amount']
        note = response.POST["add_note"]
        year = response.POST['add_year']
        month = response.POST["add_month"]
        # date = response.POST['add_date']
        # time = response.POST["add_time"]

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

    item = Data.objects.get(id = pk)
    item.delete()

    return redirect('/list')