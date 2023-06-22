from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import Movieform
from . models import display
# Create your views here.
def index(request):
    obj=display.objects.all()
    return render(request,'index.html',{'key1':obj})

def detail(request,movie_id):
    obj2=display.objects.get(id=movie_id)
    return render(request,'detail.html',{'key2':obj2})

def add(request):
    if request.method=="POST":
        name=request.POST.get('name', )
        desc=request.POST.get('desc', )
        year=request.POST.get('year', )
        img=request.FILES['img']
        movie_var=display(name=name,desc=desc,year=year,img=img)
        movie_var.save()
    return render(request,'add.html')

def update(request,id):
    movie=display.objects.get(id=id)
    form=Movieform(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'key3': form, 'key4': movie})

def delete(request,id):
    if request.method=="POST":
        movie=display.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')





