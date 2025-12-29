from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from magazin_chasek import models
from magazin_chasek import form

@login_required
def abra_items(request):
    all_tovar = models.Tovar.objects.all()
    otvet = render(request,'item.html',{'tovars':all_tovar})
    return otvet

def abra_vxod(request):
    if request.method == "GET":
        otvet = render(request,'vxod.html')
        return otvet
    else:
        name = request.POST['name']
        parol = request.POST['password']
        proshol = authenticate(request, username=name, password=parol)
        if proshol != None:
            login(request, proshol)
            k_otvet = redirect('glavnaya')
            return k_otvet
        else :
            otvet = redirect('vxod')
            return otvet
        
def abra_vixod(request):
    logout(request)
    otvet = redirect('vxod')
    return otvet

def abra_kartacka(request,chislo):
    tovar = models.Tovar.objects.get(id=chislo)
    otvet = render(request,'kartacka.html',{'tovar':tovar})
    return otvet

def abra_karzina(request):
    vsetovari = models.Karzina_tovar.objects.filter(karzina=request.user.karzina)
    otvet = render(request,'karzina.html',{'vsetovari':vsetovari})
    return otvet

def abra_plus(request):
    id = request.POST['id']
    itovar = models.Tovar.objects.get(id=id)
    ktovar = models.Karzina_tovar.objects.get(tovar=itovar, karzina=request.user.karzina)
    ktovar.kolichestvo = ktovar.kolichestvo +1
    itovar.kolichestvo = itovar.kolichestvo -1
    ktovar.save()
    itovar.save()
    otvet = redirect('karzina')
    return otvet 

def abra_minus(request):
    id = request.POST['id']
    itovar = models.Tovar.objects.get(id=id)
    ktovar = models.Karzina_tovar.objects.get(tovar=itovar, karzina=request.user.karzina)
    ktovar.kolichestvo = ktovar.kolichestvo -1
    itovar.kolichestvo = itovar.kolichestvo +1
    ktovar.save()   
    itovar.save()
    if ktovar.kolichestvo == 0:
        print(123)
        request.user.karzina.tovari.remove(itovar)
    otvet = redirect('karzina')
    return otvet 

def abra_dvk(request):
    print(request.POST)
    kartockaid = request.POST['id']
    mtog = models.Tovar.objects.get(id=kartockaid)
    spisokt = request.user.karzina.tovari.all()
    if mtog in spisokt:
        ktovar = models.Karzina_tovar.objects.get(tovar=mtog, karzina=request.user.karzina)  
        ktovar.kolichestvo = ktovar.kolichestvo+1 
        ktovar.save()
    else:
        request.user.karzina.tovari.add(mtog)
    otvet = redirect('glavnaya')
    mtog.kolichestvo = mtog.kolichestvo -1
    mtog.save()
    return otvet 
    

def abra_dik(request):
    print(request.POST)
    kartockaid = request.POST['id']
    mtog = models.Tovar.objects.get(id=kartockaid)
    tovar = models.Karzina_tovar.objects.get(tovar=mtog)
    mtog.kolichestvo = mtog.kolichestvo + tovar.kolichestvo
    mtog.save()
    request.user.karzina.tovari.remove(mtog)
    otvet = redirect('karzina')
    return otvet 

def abra_profil(request):
    otvet = render(request,'profil.html')
    return otvet
def abra_fdr(request):
    if request.method == "GET":
        fdregistrasii = form.FormDR()
        otvet = render(request,'fdr.html',{'fdr':fdregistrasii})
        return otvet
    else:
        fdregistrasii = form.FormDR(request.POST)
        if fdregistrasii.is_valid() == True:
            polzovatel = fdregistrasii.save()
            models.Karzina.objects.create(polzovatel = polzovatel)
            login(request, polzovatel)
            otvet = redirect('glavnaya')
            return otvet
        else:
            otvet = render(request,'fdr.html',{'fdr':fdregistrasii})
            return otvet
            

        
