from django.shortcuts import render,redirect
from .forms import UserForm,datachange
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from django.views.generic import CreateView,UpdateView,DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User




# def signup_user(request):
#     if request.method=='POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
           
#             form.save()
#             return redirect('login')
#     else :
#         form =UserForm()
#     return render(request,'signup.html',{'form':form})


class signup_user(CreateView):
    model = User
    template_name = 'signup.html'
    form_class= UserForm
    success_url= reverse_lazy('login')

class login_user(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('homepage')
    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)


@login_required(login_url='login')
def profile(request):
    return render(request,'profile.html')


@login_required(login_url='login')
def userlogout(request):
    logout(request)
    messages.warning(request,'Logged out Successfully')
    return redirect('homepage')



@login_required(login_url='login')
def passchange(request):
    if request.method=='POST':
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else :
        form = PasswordChangeForm(user=request.user)
    return render(request,'changepassword.html',{'form':form})



@login_required(login_url='login')
def passchangewithoutprev(request):
    if request.method=='POST':
        form =SetPasswordForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else :
        form = SetPasswordForm(user=request.user)
    return render(request,'changepassword.html',{'form':form})
    


@method_decorator(login_required(login_url='login'),name='dispatch')
class changeuserdata(UpdateView):
    model = User
    form_class = datachange
    template_name = 'changeuserdata.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'