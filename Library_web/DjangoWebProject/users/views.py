from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from management.models import BorrowBook
from django.utils.timezone import now

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff or user.is_superuser:
                return redirect('/admin/') # page for admin and superuser
            else:
                return redirect('users:common_users') # page for common users
        else:
           return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
    return render(request, 'registration/login.html')

@login_required
def common_users(request):
    # Get list of borrowed book
    borrow_list = BorrowBook.objects.filter(user=request.user)

    # Get number of overdue books
    overdue_books = borrow_list.filter(return_date__lt=now()).count()

    return render(request, 'registration/common_users.html', {
        'borrow_list': borrow_list,
        'overdue_books': overdue_books
    })