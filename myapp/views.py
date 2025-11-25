from django.shortcuts import render, redirect
from .models import UserRegistration

# 1. Login View
def login_view(request):
    if request.method == 'POST':
        # Get data from the form
        email_input = request.POST.get('email')
        password_input = request.POST.get('password')

        try:
            # Validate credentials against UserRegistration model
            user = UserRegistration.objects.get(email=email_input, password=password_input)
            
            # SUCCESS: Store user info in the session
            # This "logs them in" by creating a session cookie
            request.session['user_id'] = user.id
            request.session['user_email'] = user.email
            
            # Redirect to the protected page
            return redirect('user_list')
            
        except UserRegistration.DoesNotExist:
            # FAIL: Reload page with error message
            return render(request, 'myapp/login.html', {'error': 'Invalid email or password'})

    # If GET request, just show the form
    return render(request, 'myapp/login.html')

# 2. User List View (Protected)
def user_list_view(request):
    # Check if user is logged in (session check)
    if 'user_id' not in request.session:
        # If not logged in, kick them back to login page
        return redirect('login')

    # Retrieve all records
    users = UserRegistration.objects.all()
    
    return render(request, 'myapp/user_list.html', {'users': users})

# 3. Logout View (Optional but recommended)
def logout_view(request):
    # Clear the session
    request.session.flush()
    return redirect('login')