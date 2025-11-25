from django.shortcuts import render, redirect, get_object_or_404
from .models import UserRegistration

# ==========================================
# PART 1: AUTHENTICATION
# ==========================================

def login_view(request):
    if request.method == 'POST':
        email_input = request.POST.get('email')
        password_input = request.POST.get('password')
        try:
            # Check if user exists
            user = UserRegistration.objects.get(email=email_input, password=password_input)
            
            # Save into session
            request.session['user_id'] = user.id
            request.session['user_email'] = user.email
            return redirect('user_list')
        except UserRegistration.DoesNotExist:
            return render(request, 'myapp/login.html', {'error': 'Invalid email or password'})

    return render(request, 'myapp/login.html')

def logout_view(request):
    request.session.flush()
    return redirect('login')

# ==========================================
# PART 2: CRUD OPERATIONS
# ==========================================

# 1. READ (List Users)
def user_list_view(request):
    # Security: Check login
    if 'user_id' not in request.session:
        return redirect('login')
    
    users = UserRegistration.objects.all()
    return render(request, 'myapp/user_list.html', {'users': users})

# 2. CREATE (Add User)
def user_create_view(request):
    if 'user_id' not in request.session:
        return redirect('login')

    if request.method == 'POST':
        UserRegistration.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            password=request.POST.get('password'),
            gender=request.POST.get('gender'),
            profile_picture=request.FILES.get('profile_picture') # Handle image
        )
        return redirect('user_list')
    
    return render(request, 'myapp/user_form.html', {'title': 'Add User'})

# 3. UPDATE (Edit User)
def user_update_view(request, id):
    if 'user_id' not in request.session:
        return redirect('login')

    user = get_object_or_404(UserRegistration, id=id)

    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.gender = request.POST.get('gender')
        
        # Only update password if user typed a new one
        if request.POST.get('password'):
            user.password = request.POST.get('password')
            
        # Only update picture if user uploaded a new one
        if request.FILES.get('profile_picture'):
            user.profile_picture = request.FILES.get('profile_picture')
            
        user.save()
        return redirect('user_list')

    return render(request, 'myapp/user_form.html', {'user': user, 'title': 'Edit User'})

# 4. DELETE (Remove User)
def user_delete_view(request, id):
    if 'user_id' not in request.session:
        return redirect('login')

    user = get_object_or_404(UserRegistration, id=id)

    if request.method == 'POST':
        user.delete()
        return redirect('user_list')

    return render(request, 'myapp/user_confirm_delete.html', {'user': user})