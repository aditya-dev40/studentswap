from django.shortcuts import render

from .models import ShippingAddress, Order, OrderItem

from cart.cart import CartSession

from django.http import JsonResponse

import requests

from decimal import Decimal


# Create your views here.

def checkout(request):


    cart = CartSession(request)
    total_inr = cart.get_total()

    # fetch latest rate
    response = requests.get("https://api.exchangerate-api.com/v4/latest/INR")
    data = response.json()
    rate = Decimal(str(data["rates"]["USD"])) 
    
    total_usd = (total_inr * rate).quantize(Decimal("0.01"))

    # Users with accounts -- Pre-fill the form

    if request.user.is_authenticated:

        try:

            # Authenticated users with shipping information

            shipping_address = ShippingAddress.objects.get(user=request.user.id)

            context = {'shipping': shipping_address, 'total_usd':total_usd}

            return render(request, 'payment/checkout.html', context=context)
        
        except:

            # Authenticated users with no shipping information

            context = {
                'total_usd':total_usd
            }

            return render(request, 'payment/checkout.html', context=context)
        
    else:

        # Guest users
        
        context = {
            'total_usd':total_usd
        }

        return render(request, 'payment/checkout.html', context=context)
    
def complete_order(request):

    if request.POST.get('action') == 'post':

        name = request.POST.get('name')
        email = request.POST.get('email')

        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')

        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')

        # all-in-one shipping address

        shipping_address = (address1 + "\n" + address2 + "\n" + city + "\n" + state + "\n" + zipcode)

        # Shopping cart information

        cart = CartSession(request)

        # Get the total price of items

        total_cost = cart.get_total()

        '''
            Order variations

            1) Create order -> Account users WITH + WITHOUT shipping information 

            2) Create order -> Guest users without an account
        
        
        '''

        if request.user.is_authenticated:

            order = Order.objects.create(full_name = name, email = email, shipping_address = shipping_address,
                                            amount_paid = total_cost, user = request.user)
            

            order_id = order.pk

            for item in cart:

                OrderItem.objects.create(order_id=order_id, product=item['product'], quantity=item['qty'],
                                            price=item['price'], user=request.user )
                
        else:
            order = Order.objects.create(full_name = name, email = email, shipping_address = shipping_address,
                                            amount_paid = total_cost)
            

            order_id = order.pk

            for item in cart:

                OrderItem.objects.create(order_id=order_id, product=item['product'], quantity=item['qty'],
                                            price=item['price'])
                

        order_success = True

        response = JsonResponse({'success':order_success})

        return response

def payment_success(request):

    # clear shopping cart

    for key in list(request.session.keys()):

        if key == 'sesssion_key':

            del request.session[key]

    return render(request, 'payment/payment-success.html')

def payment_failed(request):

    return render(request, 'payment/payment-failed.html')
