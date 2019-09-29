from django.shortcuts import render
from aper.models import BookInfo

# Create your views here.
#def index(request):
#    return render(request=request,template_name='aper/index.html')
def index(request):
    booklist = BookInfo.objects.all()
    return render(request,'index.html',{'book':booklist})