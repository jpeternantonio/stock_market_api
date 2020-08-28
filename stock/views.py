from django.views.generic import ListView, UpdateView
from django.shortcuts import render, get_object_or_404
from .models import Stocks, Purchased
from .forms import PurchasedForm
from account.models import User
from django.contrib.auth.decorators import login_required



class StockListView(ListView):
    template_name = 'stock/index.html'
    context_object_name = 'stock_count'

    def get_queryset(self):
        return Stocks.objects.count()

    def get_context_data(self, **kwargs):
        context = super(StockListView, self).get_context_data(**kwargs)
        context['stocks'] = Stocks.objects.all()
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
            """
            For future implementation - appending share on existing stock

            buy_exist = Purchased.objects.values_list('stock_id').filter(user_id=u_id, stock_id=s_id)[:1]
            buy_exist_int = int(''.join(map(str, buy_exist[0])))
            if buy_exist_int == s_id:
                buy = Purchased.objects.filter(user_id=u_id, stock_id=s_id)[:1]
                buy.price = price
                buy.save()
                buy.share += share
                buy.save()
            else:
                new_buy = Purchased(user=u_id, stock=s_id, share=share, price=price)
                new_buy.save()
            """
            new_buy = Purchased(user=u_id, stock=s_id, share=share, price=price)
            new_buy.save()
            user_balance = User.objects.get(id=user_id)
            user_balance.balance -= total
            user_balance.save()
            return render(request, 'stock/buy_done.html', {'user':user})
        else:
            return render(request, 'stock/buy.html')
    else:
        return render(request, 'stock/buy.html')

@login_required(login_url="account/login")
def buy_history(request):
    user = request.user
    purchased = Purchased.objects.all().select_related('user').select_related('stock').filter(user_id=user.id).order_by('-id')
    

    context = {'purchased':purchased}
    return render(request,'stock/buy_history.html', context)

@login_required(login_url="account/login")
def sell(request, pk):
    user = request.user
    sell = Purchased.objects.get(id=pk)
    stock = Stocks.objects.get(id=sell.stock_id)
    purchased = Purchased.objects.all().filter(id=pk)
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
            user_balance = User.objects.get(id=user_id)
            user_balance.balance += total
            user_balance.save()
            sell = Purchased.objects.get(id=purchased_id)
            sell.share -= share
            sell.save()
            return render(request, 'stock/sell_done.html', {'user':user})
        else:
            return render(request, 'stock/sell.html')
    else:
        return render(request, 'stock/sell.html')