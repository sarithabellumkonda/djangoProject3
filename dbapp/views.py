from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

# Create your views here.
def input(request):
    return render(request,'input.html')
def insert(request):
    p_id=int(request.GET['t1'])
    p_name = request.GET['t2']
    p_cost = float(request.GET['t3'])
    p_mfdt = request.GET['t4']
    p_exdt = request.GET['t5']
    p1=Product(pid=p_id,pname=p_name,pcost=p_cost,pmfdt=p_mfdt,pexdt=p_exdt)
    p1.save()
    return HttpResponse("Product Inserted Successfully")
