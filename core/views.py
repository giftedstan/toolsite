from django.shortcuts import render

# Create your views here.

def home(request):
    context={
        'home_active':'active',
        'home_disabled':'disabled',
        }
    return render(request,'core/home.html',context)

def sitemap(request):
    return render(request, 'core/sitemap.xml', content_type='text/xml')