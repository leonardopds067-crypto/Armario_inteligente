from django.shortcuts import render

def index(request):
    context ={
        'titulo':'Armario de chaves',
        'Nome':'Leonardo Pereira',
    }
    return render(request,'index.html', context)

# Create your views here.

from django.http import JsonResponse 
def status_api(request): 
    return JsonResponse({'status': 'online', 'sistema': 'Key Track IoT'})
