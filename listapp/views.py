from django.shortcuts import render,redirect
from .models import dolist

# Create your views here.

def index(request):
    Pass_file=dolist.objects.all()
    if request.method== "POST":
        add_on= dolist(
            title=request.POST["title"]
        )
        add_on.save()
        return redirect("/")
        
    return render(request,"index.html",{"Pass_file":Pass_file})

def update(request, pk):
    holder=dolist.objects.get(id=pk)
    Pass_file=request.POST,isinstance=holder
    if Pass_file.is_valid():
        Pass_file.save()
        return redirect("/")


def delete(request,pk):
    Pass_file=dolist.objects.get(id=pk)
    Pass_file.delete()
    return redirect("/")
