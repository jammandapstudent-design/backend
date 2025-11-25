from django.contrib import admin
from django.urls import path
from myapp import views  # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Login URL
    path('login/', views.login_view, name='login'),
    
    # User List URL (Protected)
    path('users/', views.user_list_view, name='user_list'),
    
    # Logout URL
    path('logout/', views.logout_view, name='logout'),
    
    # Redirect root page to login (Optional convenience)
    path('', views.login_view),
]