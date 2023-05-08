from django.shortcuts import render, redirect
from user.models import UserProfile
from user.forms.ProfileForm import ProfileForm

# Create your views here.

from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        print(form)
        if form.is_valid(): #Checks if all feilds were provided
            form.save() #Saves to the database
            return redirect('login')
        else:
            return redirect('signup') #Here is possible to redirect to the error screen
    return render(request, 'user/signup.html' , {
        'form': UserCreationForm()
    })

def profile(request):
    profile = UserProfile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile,data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect(request,'user/profile.html')
    return render(request, 'user/profile.html', {
        'form':ProfileForm(instance=profile)
    })