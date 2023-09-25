from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    # Check to see if logging in
    # In home.html we made a form with a method called POST so this
    # code says is the request method a post? If so, they are filling
    # out the form so grab what they are POSTing
    if request.method == 'POST':
        # In home.html we made the input to the form name="username"
        # It is the same for password
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate, create a user variable and pass the authenticate function
        # that we imported and check if they are in the database
        user = authenticate(request, username=username, password=password)
        # If user is authenticated log them in
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging you in, please try again...")
            return redirect('home')
    # If the user is not posting send them back to the home page
    else:
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})