from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import DPC, TC, MC, DPCArea, DPCRemark, TCArea, TCRemark, MCArea, MCRemark, Shop, Shed, DPCSec, TCSec, MCSec, Status
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import HttpResponse
# Create your views here.
from http.client import HTTPResponse
from django.shortcuts import render
import pandas as pd
import os

import os.path
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from datetime import date, datetime, timedelta

import datetime as dt
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
 
import csv

def DPCExcelImport(request, Serial):
    print("---------")
    print(Serial)
    if request.method == 'POST' and request.FILES['myfile']:      
        myfile = request.FILES['myfile']
        pre = os.path.dirname(os.path.realpath(__file__))
        fs = FileSystemStorage(location=pre)
        filename = fs.save(myfile.name, myfile)
        print(filename)
        print(pre)
        uploaded_file_url = fs.url(filename)
        path = os.path.join(pre, filename)     
        empexceldata = pd.read_excel(path)        
        dbframe = empexceldata
        for dbframe in dbframe.itertuples():
            a = DPC.objects.filter(DPCName=dbframe.DPCName).first()
            e = a.POHDate
            if DPCArea.objects.filter(DPCArea=dbframe.DPCDefArea).exists():
                b = DPCArea.objects.filter(DPCArea=dbframe.DPCDefArea).first()
                print('yesDef')
                print(b)
            else:
                g = DPCArea(DPCArea=dbframe.DPCDefArea)
                print('NoSec')
                
                g.save()
                b = g
                print(b)
            if DPCSec.objects.filter(DPCSec=dbframe.DPCSecArea).exists():
                w = DPCSec.objects.filter(DPCSec=dbframe.DPCSecArea).first()
                print('yesSec')
                print(w)
            else:
                g = DPCSec(DPCSec=dbframe.DPCSecArea)
                g.save()
                w = g
                print('noSec')
                print(type(b))
            d = Status.objects.filter(Status=dbframe.DPCStatus).first()
            obj =  DPCRemark(DPCName=a,Date=str(timezone.now()),POHDate=e, DPCDefArea=b, DPCSecArea=w , DPCStatus=d, DPCDef=dbframe.DPCDef)           
            obj.save()
        p = DPC.objects.get(id=Serial)
        q = DPCRemark.objects.filter(DPCName=p.id).order_by('-Date')
        print(q)
        defi = []
        qs2 = DPCArea.objects.all()
        list1 = []
        for x in qs2:
            u = DPCRemark.objects.all().filter(POHDate=p.POHDate).filter(DPCDefArea=x.id).count()
            if u == 0:
                pass
            else:
                print(u)
                list1.append(str(u))
                defi.append(str(x.DPCArea))
            print('appended list')
            print(list1)
        context = {
            #'messages': message,
            'object': p,
            'q' : q,
            'DPC': defi,
            'freq': list1 ,
            }
        return render(request, 'deficiencies/dpcdefdet.html',context)   

def MCExcelImport(request, Serial):
    
    if request.method == 'POST' and request.FILES['myfile']:      
        myfile = request.FILES['myfile']
        pre = os.path.dirname(os.path.realpath(__file__))
        fs = FileSystemStorage(location=pre)
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        path = os.path.join(pre, filename)     
        empexceldata = pd.read_excel(path)        
        dbframe = empexceldata
        for dbframe in dbframe.itertuples():
            print("---------")
            print(dbframe)
            a = MC.objects.filter(MCName=dbframe.MCName).first()
            e = a.POHDate
            if MCArea.objects.filter(MCArea=dbframe.MCDefArea).exists():
                b = MCArea.objects.filter(MCArea=dbframe.MCDefArea).first()
                print('yesDef')
                print(b)
            else:
                g = MCArea(MCArea=dbframe.MCDefArea)
                print('NoSec')
                
                g.save()
                b = g
                print(b)
            if MCSec.objects.filter(MCSec=dbframe.MCSecArea).exists():
                w = MCSec.objects.filter(MCSec=dbframe.MCSecArea).first()
                print('yesSec')
                print(w)
            else:
                g = MCSec(MCSec=dbframe.MCSecArea)
                g.save()
                w = g
                print('noSec')
                print(type(b))
            d = Status.objects.filter(Status=dbframe.MCStatus).first()
            obj =  MCRemark(MCName=a,Date=str(timezone.now()),POHDate=e, MCDefArea=b, MCSecArea=w , MCStatus=d, MCDef=dbframe.MCDef)           
            obj.save()
        p = MC.objects.get(id=Serial)
        q = MCRemark.objects.filter(MCName=p.id).order_by('-Date')
        print(q)
        defi = []
        qs2 = MCArea.objects.all()
        list1 = []
        for x in qs2:
            u = MCRemark.objects.all().filter(POHDate=p.POHDate).filter(MCDefArea=x.id).count()
            if u == 0:
                pass
            else:
                print(u)
                list1.append(str(u))
                defi.append(str(x.MCArea))
            print('appended list')
            print(list1)
        context = {
            #'messages': message,
            'object': p,
            'q' : q,
            'DPC': defi,
            'freq': list1 ,
            }
        return render(request, 'deficiencies/mcdefdet.html',context)   

def TCExcelImport(request, Serial):
    
    if request.method == 'POST' and request.FILES['myfile']:      
        myfile = request.FILES['myfile']
        pre = os.path.dirname(os.path.realpath(__file__))
        fs = FileSystemStorage(location=pre)
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        path = os.path.join(pre, filename)     
        empexceldata = pd.read_excel(path)        
        dbframe = empexceldata
        for dbframe in dbframe.itertuples():
            print("---------")
            print(dbframe)
            a = TC.objects.filter(TCName=dbframe.TCName).first()
            e = a.POHDate
            if TCArea.objects.filter(TCCArea=dbframe.TCDefArea).exists():
                b = TCArea.objects.filter(TCCArea=dbframe.TCDefArea).first()
                print('yesDef')
                print(b)
            else:
                g = TCArea(TCCArea=dbframe.TCDefArea)
                print('NoSec')
                
                g.save()
                b = g
                print(b)
            if TCSec.objects.filter(TCSec=dbframe.TCSecArea).exists():
                w = TCSec.objects.filter(TCSec=dbframe.TCSecArea).first()
                print('yesSec')
                print(w)
            else:
                g = TCSec(TCSec=dbframe.TCSecArea)
                g.save()
                w = g
                print('noSec')
                print(type(b))
            d = Status.objects.filter(Status=dbframe.TCStatus).first()
            obj =  TCRemark(TCName=a,Date=str(timezone.now()),POHDate=e, TCDefArea=b, TCSecArea=w , TCStatus=d, TCDef=dbframe.TCDef)           
            obj.save()
        p = TC.objects.get(id=Serial)
        q = TCRemark.objects.filter(TCName=p.id).order_by('-Date')
        print(q)
        defi = []
        qs2 = TCArea.objects.all()
        list1 = []
        for x in qs2:
            u = TCRemark.objects.all().filter(POHDate=p.POHDate).filter(TCDefArea=x.id).filter(TCName=p.id).count()
            if u == 0:
                pass
            else:
                print(u)
                list1.append(str(u))
                defi.append(str(x.TCCArea))
            print('appended list')
            print(list1)
        context = {
            #'messages': message,
            'object': p,
            'q' : q,
            'DPC': defi,
            'freq': list1 ,
            }
        return render(request, 'deficiencies/tcdefdet.html',context)   




  
def export_dpc_remark(request, Serial): 
    if request.method == 'POST':
        a = DPC.objects.filter(id=Serial).first()
        p = a.POHDate
        print(p)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=f"{p}.csv"'        
        writer = csv.writer(response)
        writer.writerow([' {} Details'.format(a.DPCName)])       
        writer.writerow(['S.No','Date','DPCName','POHDate','Category','Section','Details','Status'])
 
        users = DPCRemark.objects.all().filter(DPCName=a.id).values_list('id','Date','DPCName_id','POHDate','DPCDefArea','DPCSecArea','DPCDef','DPCStatus')
        print(users)
        for user in users:
            writer.writerow(user)
        return response
 
    return render(request, 'deficiencies/dpcdefdet.html')





  

class DefiHome(LoginRequiredMixin, TemplateView):
    template_name = 'deficiencies/defhome.html'



@login_required
def DefiHome2(request):
    dpc = DPC.objects.all().order_by('-Date')
    p = []
    for n in dpc:
        k = DPCRemark.objects.all().filter(DPCName=n.id).count()
        p.append([n,k])
    tc = TC.objects.all().order_by('-Date')
    q = []
    for n in tc:
        k = TCRemark.objects.all().filter(TCName=n.id).count()
        q.append([n,k])
    mc = MC.objects.all().order_by('-Date')
    r = []
    for n in mc:
        k = MCRemark.objects.all().filter(MCName=n.id).count()
        r.append([n,k])
        
    context = {
            'dpc': p,
            'tc' : q,
            'mc' : r,
    }
    print(context)
    return render(request, 'deficiencies/defhome.html', context)

@login_required
def AddDPC(request):
    if request.method == 'POST' and request.POST.get('DPCNum').startswith("DPC")==True and request.POST.get('datepicker1') and request.POST.get('DPCShop') and request.POST.get('DPCShed'):
        print(request.POST.get('datepicker1'))
        newDPC = DPC(DPCName=request.POST.get('DPCNum'),POHDate=request.POST.get('datepicker1'),Shop=Shop.objects.get(ShopName__icontains=str(request.POST.get('DPCShop'))),Shed=Shed.objects.get(ShedName__icontains=str(request.POST.get('DPCShed'))),author=request.user)
        newDPC.save()
        message = messages.success(request, "DPC Added ")
        dpc = DPC.objects.all().order_by('-Date')
        p = []
        for n in dpc:
            k = DPCRemark.objects.all().filter(DPCName=n.id).count()
            p.append([n,k])
        tc = TC.objects.all().order_by('-Date')
        q = []
        for n in tc:
            k = TCRemark.objects.all().filter(TCName=n.id).count()
            q.append([n,k])
        mc = MC.objects.all().order_by('-Date')
        r = []
        for n in mc:
            k = MCRemark.objects.all().filter(MCName=n.id).count()
            r.append([n,k])
        
        
        context = {
                'dpc': p,
                'tc' : q,
                'mc' : r,
                
                'message' : message,
            }
        print('successful')
        return render(request, 'deficiencies/defhome.html', context)

    else:
        message = messages.warning(request, "DPC Not Added ")
        dpc = DPC.objects.all().order_by('-Date')
        p = []
        for n in dpc:
            k = DPCRemark.objects.all().filter(DPCName=n.id).count()
            p.append([n,k])
        tc = TC.objects.all().order_by('-Date')
        q = []
        for n in tc:
            k = TCRemark.objects.all().filter(TCName=n.id).count()
            q.append([n,k])
        mc = MC.objects.all().order_by('-Date')
        r = []
        for n in mc:
            k = MCRemark.objects.all().filter(MCName=n.id).count()
            r.append([n,k])
        
        
        context = {
                'dpc': p,
                'tc' : q,
                'mc' : r,
                
                'message' : message,
            }
    return render(request, 'deficiencies/defhome.html', context)
    

@login_required
def AddTC(request):
    print(request.POST.get('TCNum'))
    print(request.POST.get('datepicker'))
    if request.method == 'POST' and request.POST.get('TCNum').startswith("TC")==True and request.POST.get('datepicker') and request.POST.get('TCShop') and request.POST.get('TCShed'):
        print(request.POST.get('datepicker'))
        newTC = TC(TCName=request.POST.get('TCNum'),POHDate=request.POST.get('datepicker'),Shop=Shop.objects.get(ShopName__icontains=str(request.POST.get('TCShop'))),Shed=Shed.objects.get(ShedName__icontains=str(request.POST.get('TCShed'))),author=request.user)
        newTC.save()
        message = messages.success(request, "TC Added ")
        dpc = DPC.objects.all().order_by('-Date')
        p = []
        for n in dpc:
            k = DPCRemark.objects.all().filter(DPCName=n.id).count()
            p.append([n,k])
        tc = TC.objects.all().order_by('-Date')
        q = []
        for n in tc:
            k = TCRemark.objects.all().filter(TCName=n.id).count()
            q.append([n,k])
        mc = MC.objects.all().order_by('-Date')
        r = []
        for n in mc:
            k = MCRemark.objects.all().filter(MCName=n.id).count()
            r.append([n,k])
        
        
        context = {
                'dpc': p,
                'tc' : q,
                'mc' : r,
                
                'message' : message,
            }
        print('successful')
        return render(request, 'deficiencies/defhome.html', context)

    else:
        message = messages.warning(request, "TC Not Added ")
        dpc = DPC.objects.all().order_by('-Date')
        p = []
        for n in dpc:
            k = DPCRemark.objects.all().filter(DPCName=n.id).count()
            p.append([n,k])
        tc = TC.objects.all().order_by('-Date')
        q = []
        for n in tc:
            k = TCRemark.objects.all().filter(TCName=n.id).count()
            q.append([n,k])
        mc = MC.objects.all().order_by('-Date')
        r = []
        for n in mc:
            k = MCRemark.objects.all().filter(MCName=n.id).count()
            r.append([n,k])
        
        
        context = {
                'dpc': p,
                'tc' : q,
                'mc' : r,
                
                'message' : message,
            }
    return render(request, 'deficiencies/defhome.html', context)
    
@login_required
def AddMC(request):
    if request.method == 'POST' and request.POST.get('MCNum').startswith("MC")==True and request.POST.get('datepicker2') and request.POST.get('MCShop') and request.POST.get('MCShed'):
        newMC = MC(MCName=request.POST.get('MCNum'),POHDate=request.POST.get('datepicker2'),Shop=Shop.objects.get(ShopName__icontains=str(request.POST.get('MCShop'))),Shed=Shed.objects.get(ShedName__icontains=str(request.POST.get('MCShed'))),author=request.user)
        newMC.save()
        message = messages.success(request, "MC Added ")
        dpc = DPC.objects.all().order_by('-Date')
        p = []
        for n in dpc:
            k = DPCRemark.objects.all().filter(DPCName=n.id).count()
            p.append([n,k])
        tc = TC.objects.all().order_by('-Date')
        q = []
        for n in tc:
            k = TCRemark.objects.all().filter(TCName=n.id).count()
            q.append([n,k])
        mc = MC.objects.all().order_by('-Date')
        r = []
        for n in mc:
            k = MCRemark.objects.all().filter(MCName=n.id).count()
            r.append([n,k])
        
        
        context = {
                'dpc': p,
                'tc' : q,
                'mc' : r,
                'message' : message,
            }
        print('successful')
        return render(request, 'deficiencies/defhome.html', context)

    else:
        message = messages.warning(request, "TC Not Added ")
        dpc = DPC.objects.all().order_by('-Date')
        p = []
        for n in dpc:
            k = DPCRemark.objects.all().filter(DPCName=n.id).count()
            p.append([n,k])
        tc = TC.objects.all().order_by('-Date')
        q = []
        for n in tc:
            k = TCRemark.objects.all().filter(TCName=n.id).count()
            q.append([n,k])
        mc = MC.objects.all().order_by('-Date')
        r = []
        for n in mc:
            k = MCRemark.objects.all().filter(MCName=n.id).count()
            r.append([n,k])
        
        
        context = {
                'dpc': p,
                'tc' : q,
                'mc' : r,
                
                'message' : message,
            }
    return render(request, 'deficiencies/defhome.html', context)
    

@login_required
def showDPCdet(request, Serial):
    q = DPC.objects.get(id=Serial)
    print("--------------------**------------------")
    print(q)
    p = DPCRemark.objects.filter(DPCName=q.id).order_by('-Date')
    defi = []
    qs2 = DPCArea.objects.all()
    list1 = []
    for x in qs2:
        u = DPCRemark.objects.all().filter(POHDate=q.POHDate).filter(DPCDefArea=x.id).count()
        if u == 0:
            pass
        else:
            print(u)
            list1.append(str(u))
            defi.append(str(x.DPCArea))
        print('appended list')
        print(list1)
    
    context = {
        #'messages': message,
        'object': q,
        'q' : p,
        'DPC': defi,
        'freq': list1 ,
    }
    return render(request, 'deficiencies/dpcdefdet.html', context)

@login_required
def showTCdet(request, Serial):
    print("--------------------**------------------")
    p = TC.objects.get(id=Serial)
    q = TCRemark.objects.filter(TCName=p.id).order_by('-Date')
    print(q)
    context = {
        #'messages': message,
        'object': p,
        'q' : q,
    }
    return render(request, 'deficiencies/tcdefdet.html', context)

@login_required
def showMCdet(request, Serial):
    p = MC.objects.get(id=Serial)
    q = MCRemark.objects.filter(MCName=p.id).order_by('-Date')
    print(q)
    context = {
        #'messages': message,
        'object': p,
        'q' : q,

    }
    print(context)
    return render(request, 'deficiencies/mcdefdet.html', context)


@login_required
def addDPCRemark(request, Serial):
    if request.POST.get('Part') and request.POST.get('Def') and request.POST.get('Details') and request.POST.get('Status'):
        q = DPC.objects.filter(id=Serial).first()
        i = q.POHDate
        r = DPCArea.objects.filter(DPCArea=request.POST.get('Part')).first()
        t = DPCSec.objects.filter(DPCSec=request.POST.get('Def')).first()
        s = Status.objects.filter(Status=request.POST.get('Status')).first()
        if request.method == 'POST':
            newDef = DPCRemark(DPCName=q,POHDate=i, DPCDefArea=r, DPCSecArea=t, DPCStatus=s, DPCDef=request.POST.get('Details'))
            newDef.save()
            
            message = messages.success(request, "DPC Deficiency Record  Added: {} --> {} --> {} --> {} --> {}".format(newDef.DPCName, newDef.DPCDefArea, newDef.DPCSecArea, newDef.DPCDef, newDef.DPCStatus))
        else:
            message = messages.warning(request, "DPC Deficiency Record Not Added ")
    else:
        message = messages.warning(request, "Please Fill all Entries ")

    
    p = DPC.objects.get(id=Serial)
    q = DPCRemark.objects.filter(DPCName=p.id).order_by('-Date')
    print(q)
    defi = []
    qs2 = DPCArea.objects.all()
    list1 = []
    for x in qs2:
        u = DPCRemark.objects.all().filter(POHDate=p.POHDate).filter(DPCDefArea=x.id).filter(DPCName=p.id).count()
        if u == 0:
            pass
        else:
            print(u)
            list1.append(str(u))
            defi.append(str(x.DPCArea))
        print('appended list')
        print(list1)
    context = {
        #'messages': message,
        'object': p,
        'q' : q,
        'DPC': defi,
        'freq': list1 ,
    }
    return render(request, 'deficiencies/dpcdefdet.html', context)

@login_required
def addTCRemark(request, Serial):
    if request.POST.get('Part') and request.POST.get('Def') and request.POST.get('Details') and request.POST.get('Status'):
        q = TC.objects.filter(id=Serial).first()
        i = q.POHDate
        r = TCArea.objects.filter(TCCArea=request.POST.get('Part')).first()
        t = TCSec.objects.filter(TCSec=request.POST.get('Def')).first()
        s = Status.objects.filter(Status=request.POST.get('Status')).first()
        if request.method == 'POST':
            newDef = TCRemark(TCName=q, POHDate=i, TCDefArea=r, TCSecArea=t, TCStatus=s, TCDef=request.POST.get('Details'))
            newDef.save()
            
            message = messages.success(request, "TC Deficiency Record  Added: {} --> {} --> {} --> {} --> {} ".format(newDef.TCName,newDef.TCDefArea,newDef.TCSecArea, newDef.TCDef, newDef.TCStatus ))
        else:
            message = messages.warning(request, "TC Deficiency Record Not Added ")
    else:
        message = messages.warning(request, "Please Fill All Entries ")

    
    p = TC.objects.get(id=Serial)
    q = TCRemark.objects.filter(TCName=p.id).order_by('-Date')
    defi = []
    qs2 = TCArea.objects.all()
    list1 = []
    for x in qs2:
        u = TCRemark.objects.all().filter(POHDate=p.POHDate).filter(TCDefArea=x.id).filter(TCName=p.id).count()
        if u == 0:
            pass
        else:
            print(u)
            list1.append(str(u))
            defi.append(str(x.TCCArea))
        print('appended list')
        print(list1)
    context = {
        #'messages': message,
        'object': p,
        'q' : q,
        'DPC': defi,
        'freq': list1 ,
    }
    return render(request, 'deficiencies/tcdefdet.html', context)


@login_required
def addMCRemark(request, Serial):
    if request.POST.get('Part') and request.POST.get('Def')and request.POST.get('Details') and request.POST.get('Status'):
        q = MC.objects.filter(id=Serial).first()
        i = q.POHDate
        r = MCArea.objects.filter(MCArea=request.POST.get('Part')).first()
        t = MCSec.objects.filter(MCSec=request.POST.get('Def')).first()
        s = Status.objects.filter(Status=request.POST.get('Status')).first()
        if request.method == 'POST':
            newDef = MCRemark(MCName=q, MCDefArea=r, MCSecArea=t, MCStatus=s, MCDef=request.POST.get('Details'))
            newDef.save()
            print(newDef)
            message = messages.success(request, "MC Deficiency Record  Added: {} --> {} --> {} --> {} --> {}  ".format(newDef.MCName, newDef.MCDefArea,newDef.MCSecArea, newDef.MCDef, newDef.MCStatus))
        else:
            message = messages.warning(request, "MC Deficiency Record Not Added ")
    else:
        message = messages.warning(request, "Please Fill All Entries ")

    
    p = MC.objects.get(id=Serial)
    q = MCRemark.objects.filter(MCName=p.id).order_by('-Date')
    defi = []
    qs2 = MCArea.objects.all()
    list1 = []
    for x in qs2:
        u = MCRemark.objects.all().filter(POHDate=p.POHDate).filter(MCDefArea=x.id).filter(MCName=p.id).count()
        if u == 0:
            pass
        else:
            print(u)
            list1.append(str(u))
            defi.append(str(x.MCArea))
        print('appended list')
        print(list1)
    context = {
        #'messages': message,
        'object': p,
        'q' : q,
        'DPC': defi,
        'freq': list1 ,
    }
    return render(request, 'deficiencies/mcdefdet.html', context)

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

@login_required
def partAutocomplete(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = DPCArea.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(DPCArea__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.DPCArea
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

            return render(request, 'deficiencies/dpcdefdet.html')

@login_required
def defAutocomplete(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = DPCSec.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(DPCSec__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.DPCSec
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

            return render(request, 'deficiencies/dpcdefdet.html')




@login_required
def TCpartAutocomplete(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = TCArea.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(TCCArea__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.TCCArea
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

            return render(request, 'deficiencies/tcdefdet.html')

@login_required
def TCdefAutocomplete(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = TCSec.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(TCSec__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.TCSec
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

            return render(request, 'deficiencies/tcdefdet.html')


@login_required
def MCpartAutocomplete(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = MCArea.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(MCArea__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.MCArea
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

            return render(request, 'deficiencies/mcdefdet.html')

@login_required
def MCdefAutocomplete(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = MCSec.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(MCSec__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.MCSec
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

            return render(request, 'deficiencies/mcdefdet.html')



@login_required
def ShopAutocomplete(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = Shop.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(ShopName__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.ShopName
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

            return render(request, 'deficiencies/defhome.html')



@login_required
def ShedAutocomplete(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = Shed.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(ShedName__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.ShedName
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

            return render(request, 'deficiencies/defhome.html')



@login_required
def StatusAutocomplete(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = Status.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(Status__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.Status
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

            return render(request, 'deficiencies/dpcdefdet.html')


@login_required
def DPCChartBySection(request, Serial):
    p = DPC.objects.get(id=Serial)
    q = DPCRemark.objects.filter(DPCName=p.id).order_by('-Date')
    print(q)
    defi1 = []
    qs2 = DPCSec.objects.all()
    list11 = []
    for x in qs2:
        u = DPCRemark.objects.all().filter(POHDate=p.POHDate).filter(DPCSecArea=x.id).filter(DPCName=p.id).count()
        if u == 0:
            pass
        else:
            list11.append(str(u))
            defi1.append(str(x.DPCSec))
        print('appended list m')
    print(list11)
    print(defi1)
    context = {
        #'messages': message,
        'object': p,
        'q' : q,
        'DPC': defi1,
        'freq': list11 ,
    }
    return render(request, 'deficiencies/dpcdefdet.html', context)


@login_required
def DPCChartByArea(request, Serial):
    p = DPC.objects.get(id=Serial)
    q = DPCRemark.objects.filter(DPCName=p.id).order_by('-Date')
    print(q)
    defi1 = []
    qs2 = DPCArea.objects.all()
    list11 = []
    for x in qs2:
        u = DPCRemark.objects.all().filter(POHDate=p.POHDate).filter(DPCDefArea=x.id).filter(DPCName=p.id).count()
        if u == 0:
            pass
        else:
            list11.append(str(u))
            defi1.append(str(x.DPCArea))
        print('appended list m')
    print(list11)
    print(defi1)
    context = {
        #'messages': message,
        'object': p,
        'q' : q,
        'DPC': defi1,
        'freq': list11 ,
    }
    return render(request, 'deficiencies/dpcdefdet.html', context)



@login_required
def MCChartBySection(request, Serial):
    p = MC.objects.get(id=Serial)
    q = MCRemark.objects.filter(MCName=p.id).order_by('-Date')
    print(q)
    defi1 = []
    qs2 = MCSec.objects.all()
    list11 = []
    for x in qs2:
        u = MCRemark.objects.all().filter(POHDate=p.POHDate).filter(MCSecArea=x.id).filter(MCName=p.id).count()
        if u == 0:
            pass
        else:
            list11.append(str(u))
            defi1.append(str(x.MCSec))
        print('appended list m')
    print(list11)
    print(defi1)
    context = {
        #'messages': message,
        'object': p,
        'q' : q,
        'DPC': defi1,
        'freq': list11 ,
    }
    return render(request, 'deficiencies/mcdefdet.html', context)


@login_required
def MCChartByArea(request, Serial):
    p = MC.objects.get(id=Serial)
    q = MCRemark.objects.filter(MCName=p.id).order_by('-Date')
    print(q)
    defi1 = []
    qs2 = MCArea.objects.all()
    list11 = []
    for x in qs2:
        u = MCRemark.objects.all().filter(POHDate=p.POHDate).filter(MCDefArea=x.id).filter(MCName=p.id).count()
        if u == 0:
            pass
        else:
            list11.append(str(u))
            defi1.append(str(x.MCArea))
        print('appended list m')
    print(list11)
    print(defi1)
    context = {
        #'messages': message,
        'object': p,
        'q' : q,
        'DPC': defi1,
        'freq': list11 ,
    }
    return render(request, 'deficiencies/mcdefdet.html', context)

@login_required
def TCChartBySection(request, Serial):
    p = TC.objects.get(id=Serial)
    q = TCRemark.objects.filter(TCName=p.id).order_by('-Date')
    print(q)
    defi1 = []
    qs2 = TCSec.objects.all()
    list11 = []
    for x in qs2:
        u = TCRemark.objects.all().filter(POHDate=p.POHDate).filter(TCSecArea=x.id).filter(TCName=p.id).count()
        if u == 0:
            pass
        else:
            list11.append(str(u))
            defi1.append(str(x.TCSec))
        print('appended list m')
    print(list11)
    print(defi1)
    context = {
        #'messages': message,
        'object': p,
        'q' : q,
        'DPC': defi1,
        'freq': list11 ,
    }
    return render(request, 'deficiencies/tcdefdet.html', context)


@login_required
def TCChartByArea(request, Serial):
    p = TC.objects.get(id=Serial)
    q = TCRemark.objects.filter(TCName=p.id).order_by('-Date')
    print(q)
    defi1 = []
    qs2 = TCArea.objects.all()
    list11 = []
    for x in qs2:
        u = TCRemark.objects.all().filter(POHDate=p.POHDate).filter(TCDefArea=x.id).filter(TCName=p.id).count()
        if u == 0:
            pass
        else:
            list11.append(str(u))
            defi1.append(str(x.TCCArea))
        print('appended list m')
    print(list11)
    print(defi1)
    context = {
        #'messages': message,
        'object': p,
        'q' : q,
        'DPC': defi1,
        'freq': list11 ,
    }
    return render(request, 'deficiencies/tcdefdet.html', context)

