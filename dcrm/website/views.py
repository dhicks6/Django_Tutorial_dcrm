from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Here we import the forms that we have made so we can use them here in views.py
from .forms import SignUpForm, AddRecordForm
from .models import Record
def home(request):
    # .all gets all of the records
    records = Record.objects.all()


    # Check to see if logging in.
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
        return render(request, 'home.html', {'records':records })


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')

def register_user(request):
    # This if statement is if they are POSTing or filling out the form.
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            #form.cleaned_data pulls out the username and assigns it to this username.
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Why not password1? Because we assigned the data in password1 to the var password 1 line above
            user = authenticate(username=username, password=password)
            login(request, user)
            # If successful
            messages.success(request, "You have successfully registered! Welcome!")
            # After logging them in we want to send them to the homepage
            return redirect('home')
    # This else is for if they are not POSTing the form so just going to the website.

    # Here were not passing in the request because they have not filled out the form they are just going to
        # the page. They may want to fill out the form but they have not done it yet.

    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look up record
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "You must be logged in to view that page...")
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record Deleted Successfully")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to do that...")
        return redirect('home')

def add_record(request):
    # Here the or none says if they are not posting just go to the webpage
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added...")
                return redirect('home')
        # {'form':form} says if they are not filling out the form we need to pass them
        #  the form so they can fill it out
        return render(request, 'add_record.html', {'form':form})
    # if they are not authenticated
    else:
        # Send a message
        messages.success(request, "You must be logged in...")
        # Return them to the home page to login
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        # Assign the record at primary key id to current_record so we can update it
        current_record = Record.objects.get(id=pk)
        # Here we pass an instance of current_record to the page
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated...")
            # Return them to the home page to login
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "Must be logged in...")
        return redirect('home')
