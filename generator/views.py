from django.http import request
from django.shortcuts import redirect, render
import requests
import re


# Create your views here.
def mainapp(request):

    
    

    email = request.GET.get('email')
    name = request.GET.get('name')

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    try:

        if(re.fullmatch(regex, email)):
            
            url = "https://team.gdrive.vip/drive"
            json_data = {'emailAddress': email, 'teamDriveName': name, 'teamDriveThemeId': 'random'}
            print(json_data)
            header = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}


            get_drive = requests.post(url, json=json_data, headers=header, verify=False, )
            print(get_drive.status_code)

            if get_drive.status_code == 200:
                return redirect(success_page)
        
        else:
            return redirect(error_page)
        
    except:
        
        x = 1
    



    context = {
        'email' : email,
        'name' : name,
    }



    
    return render(request, 'index.html')

def error_page(request):
    return render(request, 'error.html')

def success_page(request):
    return render(request, 'success.html')



def handle404(request, exception):
 return render(request, 'error.html', status=404)