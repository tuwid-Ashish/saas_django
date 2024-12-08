from django.http import HttpResponse
from django.shortcuts import render
from visits.models import Pagevists

def home_view(request,*args,**kwargs):
    home_template = "home.html"
    Pagevists.objects.create(path=request.path)
    page_count = Pagevists.objects.count()
    context = {
        "page_count": page_count,
        "path": request.path
    }
    return render(request,home_template,context)