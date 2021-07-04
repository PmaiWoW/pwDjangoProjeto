from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "prices3D_SPA"

urlpatterns = [
    path('price-guide-3d', views.price_guide_3d_page_view, name='price-guide-3d'),
]