from django.shortcuts import render

# Create your views here.

def price_guide_3d_page_view(request):
    context = {
        'headerText': "Price Guide - 3D Modeling and Texturing",
    }
    return render(request, 'prices3D_SPA/price-guide-3d.html', context)
