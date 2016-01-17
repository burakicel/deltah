from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, OfferForm
from django.contrib.auth.decorators import login_required
from .models import Enterprise, Offer
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
