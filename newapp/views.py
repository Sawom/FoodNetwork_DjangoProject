from django.shortcuts import redirect, render
from .models import customer
from .models import order

# Customer form
def home(request):
    customer_list = customer.objects.order_by("customer_id")
    diction = {"customer": customer_list}
    
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('name')
        age =  request.POST.get('age')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        email = request.POST.get('email')
        phone =  request.POST.get('phone')

        customer.objects.create(customer_name= name,age=age,height_cm=height ,weight_kg=weight,email=email,phone_no=phone)
        return redirect("webpage1")

    return render(request, 'index.html',context=diction)

#order form
def orders(request):
    order_list = order.objects.order_by("order_id")
    diction = {"order": order_list}

    if request.method == 'POST':
        print(request.POST)
        food_id = request.POST.get('food_id')

        cust = customer.objects.get(customer_id=request.POST.get('customer_id'))
        food_quantity = request.POST.get('food_quantity')
        food_category = request.POST.get('food_category')
        total_price_taka = request.POST.get('total_price_taka')
        order_location = request.POST.get('order_location')
        order_status = request.POST.get('order_status')

        order.objects.create(food_id=food_id,customer_id=cust,food_quantity=food_quantity,food_category=food_category,total_price_taka=total_price_taka,order_location=order_location,order_status=order_status)
        return redirect("webpage5")

    return render(request, 'order.html',context=diction)


def webpage2(request):
    return render(request,'breakfast.html')

def webpage3(request):
    return render(request,'lunch.html')

def webpage4(request):
    return render(request,'dinner.html')

def webpage5(request):
    return render(request,'order.html')
