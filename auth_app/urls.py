from django.urls import path
from auth_app.views import *

urlpatterns = [
     path('admin/login/', admin_login, name='admin-login'),
     path('logout/', logout_view, name='logout'),
]