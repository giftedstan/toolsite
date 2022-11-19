from django.contrib import admin
from django.urls import path,include
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('sitemap.xml',views.sitemap,name='sitemap'),
    path('pinterest/', include('pinterest_downloader.urls')),
    path('youtube/', include('youtube_downloader.urls')),
    path('instagram/', include('reels_downloader.urls')),
    path('tiktok/', include('tiktok_downloader.urls')),
    path('template/', include('temp_downloader.urls')),
    path('facebook/', include('facebook_downloader.urls'))
]