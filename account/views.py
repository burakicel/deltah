from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, OfferForm, TransactionForm
from django.contrib.auth.decorators import login_required
from .models import Enterprise, Customer, Offer, Transaction
from django.http import HttpResponseRedirect


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    acc = Enterprise.objects.filter(user=request.user)
    if acc:
        return render(request,'account/dashboard_ent.html', {'section': 'dashboard'})
    else:
        return render(request,'account/dashboard_cus.html', {'section': 'dashboard', 'name': request.user.username})

@login_required
def offer(request):
    acc = Enterprise.objects.filter(user=request.user)
    if acc:
        if request.method == 'POST':
            form = OfferForm(request.POST)
            if form.is_valid:
                new_offer = Offer.objects.create(name=form['name'].data, quantity=form['quantity'].data, enterprise=acc[0],
                    product_title=form['product_title'].data,reward=form['reward'].data)
                new_offer.save()
                return HttpResponseRedirect("../")
            else:
                return HttpResponse('Unvalid Data')
        else:
            form = OfferForm()

        return render(request, 'account/offer.html',{'form': form})
    else:
        return HttpResponse('Not Available')

@login_required
def transaction(request):
    acc = Enterprise.objects.filter(user=request.user)
    if acc:
        if request.method == 'POST':
            form = TransactionForm(request.POST)
            if form.is_valid:
                new_offer = Transaction.objects.create(enterprise=acc[0],price=form['price'].data,offer=Offer.objects.get(id=form['offer'].data),customer=Customer.objects.get(id=form['customer'].data))
                new_offer.save()
                return HttpResponseRedirect("../")
            else:
                return HttpResponse('Unvalid Data')
        else:
            form = TransactionForm()

        return render(request, 'account/transaction.html',{'form': form})
    else:
        return HttpResponse('Not Available')

@login_required
def deals(request):
    acc = Customer.objects.filter(user=request.user)
    offers = Offer.objects.all()
    trans = Transaction.objects.all()
    output = []

    for offer in offers:
        elem = []
        elem.append(offer.name)
        counter = 0
        for transaction in trans:
            if transaction.customer == acc[0]:
                if transaction.enterprise == offer.enterprise:
                    if transaction.offer == offer:
                        counter=counter+1;
        elem.append(counter)
        elem.append(offer.quantity)
        calc = float("{0:.2f}".format(((float(counter)/offer.quantity)*100)))
        elem.append(calc)
        if (calc < 100) and (calc>0):
            output.append(elem)

    if acc:
        return render(request, 'account/deals.html',{'output': output})
    else:
        return HttpResponse('Not Available')

@login_required
def rewards(request):
    acc = Customer.objects.filter(user=request.user)
    offers = Offer.objects.all()
    trans = Transaction.objects.all()
    output = []

    for offer in offers:
        elem = []
        elem.append(offer.name)
        counter = 0
        for transaction in trans:
            if transaction.customer == acc[0]:
                if transaction.enterprise == offer.enterprise:
                    if transaction.offer == offer:
                        counter=counter+1;
        elem.append(counter)
        elem.append(offer.quantity)
        calc = float("{0:.2f}".format(((float(counter)/offer.quantity)*100)))
        elem.append(calc)
        if (calc >= 100):
            output.append(offer.reward)

    if acc:
        return render(request, 'account/rewards.html',{'output': output})
    else:
        return HttpResponse('Not Available')


@login_required
def history(request):
    acc = Customer.objects.filter(user=request.user)
    if acc[0]:
        offers = Offer.objects.all()
        trans = Transaction.objects.all()
        output = []
        for transaction in trans:
            elem = []
            if transaction.customer == acc[0]:
                elem.append(transaction.enterprise)
                elem.append(transaction.price)
                elem.append(transaction.offer)
                elem.append(transaction.date)
            output.append(elem)


        if acc:
            return render(request, 'account/history.html',{'output': output[::-1]})
        else:
            return HttpResponse('Not Available')
