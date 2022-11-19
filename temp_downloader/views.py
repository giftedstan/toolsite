from django.shortcuts import render,redirect
from .models import TemplateRecord
from .forms import TemplateDownloadForm
from django.contrib import messages
import requests as r
import mechanize
from bs4 import BeautifulSoup
import requests


# Create your views here.

def index(request):    
    if request.method=='POST':
        fm=TemplateDownloadForm(request.POST)
        if fm.is_valid():
            query=fm.cleaned_data['temp']
            
        try:
            br = mechanize.Browser()
            br.set_handle_robots(False)
            br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
            _url = 'https://nullphpscript.com/?s='
            q = query.replace(' ', '+')
            url = _url+q

            br.open(url)
            html = br.response().read()
            soup = BeautifulSoup(html,'html.parser')
            container = soup.select('.td-block-span6')
            formatted_data = []
            for content in container:
                title = content.find('h3', class_='entry-title').a.text
                link = content.find('h3', class_='entry-title').a['href']

                data = {
                    'title': title,
                    "url": link
                }

                r = requests.get(link).content
                soup = BeautifulSoup(r,'html.parser')
                image = soup.find('div', class_='td-module-thumb').a.img['src']
                description = soup.find('div', class_='td-post-content').p.text
                demo = soup.select_one('.download-link-section').find_previous('a')['href']


                download_links = soup.select('.copybox')
                d_links = []
                for link in download_links:
                    d_li = link.find('input')['value']
                    d_links.append(d_li)

                data['image'] = image
                data['description'] = description
                data['download_links'] = d_links
                data['demo'] = demo


                formatted_data.append(data)

    
        except:
            messages.warning(request,'Sorry something went wrong !!')
            return redirect('temp_index')
        context={
            'template_active':'active',
            'template_disabled':'disabled',
            'form':fm,
            'download':True,
            'sdvideo_url':'video',
            'hdvideo_url':'video',
            'template': formatted_data
            }
    else:
        fm=TemplateDownloadForm()
        context={
            'template_active':'active',
            'template_disabled':'disabled',
            'form':fm
            }
    return render(request,'template_downloader/template.html',context)
