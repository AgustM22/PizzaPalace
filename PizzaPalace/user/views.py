from django.shortcuts import render, redirect


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
"""
def login(request):
    
    if request.method == 'POST':
        username = request.POST['UserName']
        password = request.POST['Password']
        user = MyBackend.authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            # Invalid login
            return redirect('login')
    return render(request, 'user/login.html' , {
        'form': LoginForm()
    })
"""