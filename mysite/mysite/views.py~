from django.http import HttpResponse
import datetime
from django.shortcuts import render
from paintapp.models import pic_store #database access
from django.views.decorators.csrf import csrf_exempt #for security checking

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def welcome(request):
    return render(request, 'paint.html') #load html file

@csrf_exempt
def post_picture(request): #store jsondata, title in database
    name=request.POST.get('name')
    data=request.POST.get('data')
    insert=pic_store(name=name, data=data)
    insert.save()
    return render(request, 'paint.html')

def recent(request): #all stored values
    posts=[dict(id=i.id, title=i.name) for i in pic_store.objects.order_by('id')]
    return render(request, 'recent.html', {'posts': posts})

def load(request, filename): #reload picture
    posts=[dict(id=i.id, title=i.name, data=i.data) for i in pic_store.objects.filter(name=filename)]
    return render(request, 'picload.html', {'posts' :posts} ) 
