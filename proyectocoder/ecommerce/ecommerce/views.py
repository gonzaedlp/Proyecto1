from django.http import HttpResponse
from django.shortcuts import render

def base(request):
    context={}
    return render(request,"index.html",context=context)

