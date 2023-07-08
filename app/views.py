from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.contrib.auth.decorators import login_required
from app.models import *
from app.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from rest_framework import viewsets
from app.serializers import *

from rest_framework.response import Response
from django.views.generic import CreateView

def home(request):
    if request.session.get('username'):
        username = request.session.get('username')
        d={'username':username}

        return render(request,'home.html',d)
    return render(request,'home.html')


def Register(request):
    UFO = UserForm()
    d={'UFO':UFO}
    if request.method == 'POST':
        UFO = UserForm(request.POST)
        if UFO.is_valid():
            NUFO=UFO.save(commit=False)
            password=UFO.cleaned_data['password']
            NUFO.set_password(password)
            NUFO.save()
            return HttpResponse("Registeration done successfully")

    return render(request,'Register.html',d)


def user_login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        AUO=authenticate(username=username,password=password)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('invalid username or password')
    

    return render(request,'user_login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))



@login_required
def insert_data(request):
    d={'CFO':ChocolateForm()}
    if request.method =='POST' and request.FILES:
        CO = ChocolateForm(request.POST,request.FILES)
        if CO.is_valid():
            CO.save()
            return HttpResponse("The data is inserted")
        else:
            return HttpResponse("the data is not valid")
    

    return render(request,'insert_data.html',d)

class ChocolateData(viewsets.ViewSet):
    def list(self,request):
        ADO=Chocolate.objects.all()
        SJD=ChocolateMS(ADO,many=True)
        d={'data':SJD.data}
        return render(request,'list.html',d)

    def retrieve(self,request,pk):
        TO=Chocolate.objects.get(pk=pk)
        SDO=ChocolateMS(TO)
        return Response(SDO.data)

    def update(self,request,pk):
        SPO=Chocolate.objects.get(pk=pk)
        SPD=ChocolateMS(SPO,data=request.data)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'chocolate is updated'})
        else:
            return Response({'Failed':'chocolate is Not Updated'})
    
    def partial_update(self,request,pk):
        SPO=Chocolate.objects.get(pk=pk)
        SPD=ChocolateMS(SPO,data=request.data,partial=True)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'chocolate is updated'})
        else:
            return Response({'Failed':'chocolate is Not Updated'})
    def destroy(self,request,pk):
        Chocolate.objects.get(pk=pk).delete()
        return Response({'Deleted':'chocolate is deleted'})


    



