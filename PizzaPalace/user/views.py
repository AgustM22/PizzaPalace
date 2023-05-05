from django.shortcuts import render, redirect
from user.forms.signupform import SignUpForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.data)
            return redirect('signup') #Here is possible to redirect to the error screen
    return render(request, 'user/signup.html' , {
        'form': SignUpForm()
    })