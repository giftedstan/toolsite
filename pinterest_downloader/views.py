from django.shortcuts import render,redirect
from .models import PinterestRecord
from .forms import PinterestDownloadForm
from django.contrib import messages
import requests as r
import mechanize
from bs4 import BeautifulSoup


# Create your views here.

def index(request):    
    if request.method=='POST':
        fm=PinterestDownloadForm(request.POST)
        if fm.is_valid():
            link=fm.cleaned_data['link']
            
        try:
            br = mechanize.Browser()
            br.set_handle_robots(False)
            br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
            br.open('https://pinterestvideodownloader.com/')
            br.select_form(nr=0)
            br.form['url'] = str(link)
            br.submit()

            video_html = br.response().read()
            soup = BeautifulSoup(video_html,'html.parser')
            video = soup.select_one("video")['src']
            image = soup.select(".more-link")[2]['href']
            
            # print("Here's your Video Link: {video} \n\n***********************\n\nHere's is your image download link: {image}".format(video=video, image=image))

    
        except:
            messages.warning(request,'Sorry something went wrong !!')
            return redirect('pinterest_index')
        context={
            'pinterest_active':'active',
            'pinterest_disabled':'disabled',
            'form':fm,
            'download':True,
            'sdvideo_url':video,
            'hdvideo_url':image,
            }
    else:
        fm=PinterestDownloadForm()
        context={
            'pinterest_active':'active',
            'pinterest_disabled':'disabled',
            'form':fm
            }
    return render(request,'pinterest_downloader/pinterest.html',context)
