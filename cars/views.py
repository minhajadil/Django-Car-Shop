from django.shortcuts import render,redirect
from .models import Car
from django.contrib.auth.decorators import login_required
# Create your views here.
from userauth.forms import CommentForm
from userauth.models import Comment



def detail(request,id):
    carr = Car.objects.get(pk=id)
    comments= Comment.objects.filter(car=carr)

    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = carr
            comment.save()
            return redirect('details',id=id)
    else :
        form = CommentForm()
    
    return render(request,'car_details.html',{'car':carr,'form':form,'comment':comments})

@login_required(login_url='login')
def buy(request,id):
    carr = Car.objects.get(pk=id)
    carr.quantity = carr.quantity-1
    carr.save()
    request.user.bought_cars.add(carr)
    return render(request,'car_details.html',{'car':carr})