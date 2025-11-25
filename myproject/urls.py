from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views   # <--- CHANGED: Import from 'myapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Login & Auth
    path('', views.login_view),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # CRUD Operations
    path('users/', views.user_list_view, name='user_list'),
    path('add/', views.user_create_view, name='user_create'),
    path('update/<int:id>/', views.user_update_view, name='user_update'),
    path('delete/<int:id>/', views.user_delete_view, name='user_delete'),
]

# Allow image serving during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)