# views.py
from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
from datetime import datetime

def users_list(request):
    users = User.objects.all()  # Fetch all users
    today = datetime.today().date()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user data to the database
            return redirect('users_list')  # Redirect to the same page to avoid resubmission
    else:
        form = UserForm()

    return render(request, 'users_list.html', {'users': users, 'today': today, 'form': form})
