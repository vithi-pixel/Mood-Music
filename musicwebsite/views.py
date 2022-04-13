from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html',{})


def about(request):
    return render(request,'about.html',{})

def calm(request):
    return render(request,'calm.html',{})

def sad(request):
    return render(request,'sad.html',{})   


def happy(request):
    return render(request,'happy.html',{})

def party(request):
    return render(request,'party.html',{})

def angry(request):
    return render(request,'angry.html',{})