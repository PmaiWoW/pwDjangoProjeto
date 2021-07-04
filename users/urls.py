from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "users"

urlpatterns = [
    path('home', views.index_page_view, name='home'),
    path('login', views.login_page_view, name='login'),
    path('logout', views.logout_page_view, name='logout'),
]