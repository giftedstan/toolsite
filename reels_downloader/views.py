from django.shortcuts import render,redirect
from .models import ReelsRecord
from .forms import ReelsDownloadForm
from django.contrib import messages
import requests as r
import mechanize
from bs4 import BeautifulSoup


# Create your views here.

def index(request):    
    if request.method=='POST':
        fm=ReelsDownloadForm(request.POST)
        if fm.is_valid():
            link=fm.cleaned_data['link']
            
        try:
            br = mechanize.Browser()
            br.set_handle_robots(False)
            br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
            br.open("https://www.expertsphp.com/instagram-reels-downloader.php")
            br.select_form(nr=0)
            br.form['url'] = str(link)
            br.submit()

            video_html = br.response().read()
            soup = BeautifulSoup(video_html,'html.parser')
            video = soup.select_one("source")['src']
            # image = soup.select("table")
            # soup.find("td").find_next_sibling("a")
            # print(image)
            
            # print("Here's your Video Link: {video} \n\n***********************\n\nHere's is your image download link: {image}".format(video=video, image=image))

    
        except:
            messages.warning(request,'Sorry something went wrong !!')
            return redirect('reels_index')
        context={
            'reels_active':'active',
            'reels_disabled':'disabled',
            'form':fm,
            'download':True,
            'sdvideo_url':video,
            'hdvideo_url':video,
            }
    else:
        fm=ReelsDownloadForm()
        context={
            'reels_active':'active',
            'reels_disabled':'disabled',
            'form':fm
            }
    return render(request,'reels_downloader/reels.html',context)
