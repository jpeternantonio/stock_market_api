import random
from django.views.generic import ListView, UpdateView
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum, F, ExpressionWrapper, DecimalField
from .models import Stocks, Purchased
from .forms import PurchasedForm, BuyForm
from account.models import User
from decimal import Decimal
from django.contrib.auth.decorators import login_required



class StockListView(ListView):
    template_name = 'stock/index.html'
    
    context_object_name = 'stock_count'

    def get_queryset(self):
        queryset = Stocks.objects.count()

    def get_context_data(self, **kwargs):
        stock = Stocks.objects.values('id')
        odd = []
        even = []
        for i in stock:
            if i['id'] % 2 == 0:
                even.append(i['id'])
            else:
                odd.append(i['id'])
        odd_tuple = tuple(odd)
        even_tuple = tuple(even)
        context = super(StockListView, self).get_context_data(**kwargs)
        context['stocks'] = Stocks.objects.filter(id__in=odd_tuple).update(price=F('price') + random.uniform(-19.5, 19.5))
        context['stocks'] = Stocks.objects.filter(id__in=even_tuple).update(price=F('price') + random.uniform(-19.5, 19.5))
        context['stocks'] = Stocks.objects.all().filter(price__gte=1)
        return context



@login_required(login_url="account/login")
def buy_stock(request, pk):
    stock = Stocks.objects.get(id=pk)
    user = request.user
   
    
    context = {'stock':stock,
               'user':user,
            }
    
    return render(request, 'stock/buy.html', context)


@login_required(login_url="account/login")
def buy_done(request):
    user = request.user
    if request.method == 'POST':
        if request.POST['s_name'] and request.POST['s_price'] and request.POST['share'] and request.POST['user_id'] and request.POST['stock_id']:

            stock_id = request.POST['stock_id']
            price = float(request.POST['s_price'])
            share = float(request.POST['share'])
            user_id = request.POST['user_id']
            total = price * share

            u_id = User.objects.get(id=user_id)
            s_id = Stocks.objects.get(id=stock_id)
            user_balance = User.objects.get(id=user_id)
            if total > user_balance.balance:
                return render(request, 'stock/buy.html', {'error':"You don't have enough balance"})
            user_balance.balance -= total
            user_balance.save()
            new_buy = Purchased(user=u_id, stock=s_id, share=share, price=price)
            new_buy.save()
           
    
            return render(request, 'stock/buy_done.html', {'user':user, 'total':total})
        else:
            return render(request, 'stock/buy.html')
    else:
        return render(request, 'stock/buy.html')


@login_required(login_url="account/login")
def buy_history(request):
    user = request.user
    purchased = (Purchased.objects
                .annotate(invested=ExpressionWrapper(F('share') * F('price'), output_field=DecimalField()))
                .annotate(current_price=ExpressionWrapper(F('share') * F('stock__price'), output_field=DecimalField()))
                .filter(user_id=user.id)).filter(share__gte=1).order_by('-id')
    context = {'purchased':purchased}
    return render(request,'stock/buy_history.html', context)


@login_required(login_url="account/login")
def sell(request, pk):
    user = request.user
    sell = Purchased.objects.get(id=pk)
    stock = Stocks.objects.get(id=sell.stock_id)
    purchased = Purchased.objects.values('id', 'share').filter(id=pk)
    user = request.user
    context = {
               'user':user,
               'stock':stock,
               'purchased':purchased,
           
            }
    
    return render(request, 'stock/sell.html', context)


@login_required(login_url="account/login")
def sell_done(request):
    user = request.user
    if request.method == 'POST':
        if request.POST['s_name'] and request.POST['s_price'] and request.POST['share'] and request.POST['user_id'] and request.POST['purchased_id']:

            price = float(request.POST['s_price'])
            purchased_id = request.POST['purchased_id']
            share = float(request.POST['share'])
            user_id = request.POST['user_id']
            total = price * share
            #total = request.POST['total']

            u_id = User.objects.get(id=user_id)
            sell = Purchased.objects.get(id=purchased_id)
            if share <= 0:
                return render(request, 'stock/sell.html', {'error':"You enter an invalid number"})
            if share > sell.share:
                return render(request, 'stock/sell.html', {'error':"You enter more than your share"})
            sell.share -= share
            sell.save()
            user_balance = User.objects.get(id=user_id)
            user_balance.balance += total
            user_balance.save()
            return render(request, 'stock/sell_done.html', {'user':user, 'total':total})
        else:
            return render(request, 'stock/sell.html')
    else:
        return render(request, 'stock/sell.html')