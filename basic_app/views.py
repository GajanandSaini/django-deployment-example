from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict= {'text':"Hello World",'number':100}
    return render(request,'basic_app/index.html',context_dict)


def base(request):
    return render(request,'basic_app/base.html')



def relative(request):
    return render(request,'basic_app/relative_url.html')


def others(request):
    return render(request,'basic_app/others.html')
