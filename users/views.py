from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm



# Create your views here.
def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #it will hash the password
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your Account has  been created! You are now able to login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
        return render(request,'users/register.html',{'form': form})
    

@login_required
def profile(request):
    return render(request, 'users/profile.html')


#messages.debug
#messages.success


 