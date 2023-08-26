from django.shortcuts import render
from django.db.models import Q
from datetime import date, datetime, timedelta
from django.contrib.auth.decorators import login_required
from defi.models import DPC, TC, MC, DPCArea, DPCRemark, MCArea, MCRemark, TCArea, TCRemark, DPCSec, TCSec, MCSec
from django.db.models import Avg, Sum
from django.utils import timezone
# Create your views here.

@login_required
def chartshome(request):
    currdate = date.today()
    context = {
        'time': currdate,
    }
    return render(request, 'charts/chartshome.html', context)


@login_required
def dpcchart(request):
    currdate = date.today()
    print(request.POST.get('datepicker6'))
    qs6 = DPC.objects.all().order_by('-POHDate').filter(POHDate__lt=request.POST.get('datepicker1'), POHDate__gt=request.POST.get('datepicker2'))
    qs4 = DPCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=request.POST.get('datepicker1'), POHDate__gt=request.POST.get('datepicker2'))
    if request.POST.get('DPCPart'):
        lo = DPCArea.objects.get(DPCArea=request.POST.get('DPCPart'))
    if request.POST.get('DPCDef'):
        po = DPCSec.objects.get(DPCSec=request.POST.get('DPCDef'))
    if not request.POST.get('DPCPart') and not request.POST.get('DPCDef'):
        defi = []
        list1 = []
        for x in qs6:
            qr = qs4.filter(DPCName=x.id)
            q = qr.count()
            if q != 0:
                list1.append(str(q))
        list2 = []
        for x in qs6:
            qr = qs4.filter(DPCName=x.id)
            q = qr.count()
            print(q)
            if q != 0:
                defi.append(str(x.DPCName))
                p = qr
                for x in p:
                    list2.append(x)
                    print(p)
            else:
                pass
                print(list2)
        context = {
            'DPC': defi,
            'time': currdate,
            'freq': list1,
            'RolStock' : 'DPC',
            'PartDisplay' : '',
            'SectionDisplay' : '',
            'from' : request.POST.get('datepicker1'),
            'to' : request.POST.get('datepicker2'),
            'q' : list2,
        }
    if request.POST.get('DPCPart') and not request.POST.get('DPCDef'):
        defi = []
        list1 = []
        for x in qs6:
            qr = qs4.filter(DPCName=x.id)
            q = qr.filter(DPCDefArea=lo.id).count()
            if q != 0:
                list1.append(str(q))
        list2 = []
        for x in qs6:
            qr = qs4.filter(DPCName=x.id)
            q = qr.filter(DPCDefArea=lo.id).count()
            if q != 0:
                defi.append(str(x.DPCName))
                p = qr.filter(DPCDefArea=lo.id)
                for x in p:
                    list2.append(x)
                    print(p)
            else:
                pass
        context = {
            'DPC': defi,
            'time': currdate,
            'freq': list1,
            'RolStock' : 'DPC',
            'PartDisplay' : lo.DPCArea,
            'SectionDisplay' : '',
            'from' : request.POST.get('datepicker5'),
            'to' : request.POST.get('datepicker6'),
            'q' : list2,
        }
    elif request.POST.get('DPCDef') and not request.POST.get('DPCPart'):
        defi = []
        list1 = []
        for x in qs6:
            qr = qs4.filter(DPCName=x.id)
            q = qr.filter(DPCSecArea=po.id).count()
            if q != 0:
                list1.append(str(q))
        list2 = []
        for x in qs6:
            qr = qs4.filter(DPCName=x.id)
            q = qr.filter(DPCSecArea=po.id).count()
            if q != 0:
                defi.append(str(x.DPCName))
                p = qr.filter(DPCSecArea=po.id)
                for x in p:
                    list2.append(x)
                    print(p)
            else:
                pass

        context = {
            'DPC': defi,
            'time': currdate,
            'freq': list1,
            'RolStock' : 'DPC',
            'PartDisplay' : '',
            'SectionDisplay' : po.DPCSec,
            'from' : request.POST.get('datepicker5'),
            'to' : request.POST.get('datepicker6'),
            'q' : list2,
        }
    elif request.POST.get('DPCDef') and request.POST.get('DPCPart'):
        defi = []
        list1 = []
        for x in qs6:
            qr = qs4.filter(DPCName=x.id)
            q = qr.filter(DPCSecArea=po.id).filter(DPCDefArea=lo.id).count()
            if q != 0:
                list1.append(str(q))
        list2 = []
        for x in qs6:
            qr = qs4.filter(DPCName=x.id)
            q = qr.filter(DPCSecArea=po.id).filter(DPCDefArea=lo.id).count()
            print(q)
            if q != 0:
                defi.append(str(x.DPCName))
                p = qr.filter(DPCSecArea=po.id).filter(DPCDefArea=lo.id)
                for x in p:
                    list2.append(x)
                    print(p)
            else:
                pass
                print(list2)
        context = {
            'DPC': defi,
            'time': currdate,
            'freq': list1,
            'RolStock' : 'DPC',
            'PartDisplay' : lo.DPCArea,
            'SectionDisplay' : po.DPCSec,
            'from' : request.POST.get('datepicker5'),
            'to' : request.POST.get('datepicker6'),
            'q' : list2,
        }
    return render(request, 'charts/chartshome.html', context)


@login_required
def tcchart(request):
    currdate = date.today()
    qs6 = TC.objects.all().order_by('-POHDate').filter(POHDate__lt=request.POST.get('datepicker4'), POHDate__gt=request.POST.get('datepicker3'))
    qs4 = TCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=request.POST.get('datepicker4'), POHDate__gt=request.POST.get('datepicker3'))
    if request.POST.get('TCPart'):
        lo = TCArea.objects.get(TCCArea=request.POST.get('TCPart'))
    print(request.POST.get('TCDef'))
    if request.POST.get('TCDef'):
        po = TCSec.objects.get(TCSec=request.POST.get('TCDef'))
    if not request.POST.get('TCPart') and not request.POST.get('TCDef'):
        defi = []
        list1 = []
        for x in qs6:
            qr = qs4.filter(TCName=x.id)
            q = qr.count()
            if q != 0:
                list1.append(str(q))
        list2 = []
        for x in qs6:
            qr = qs4.filter(TCName=x.id)
            q = qr.count()
            print(q)
            if q != 0:
                defi.append(str(x.TCName))
                p = qr
                for x in p:
                    list2.append(x)
                    print(p)
            else:
                pass
                print(list2)
        context = {
            'DPC': defi,
            'time': currdate,
            'freq': list1,
            'RolStock' : 'TC',
            'PartDisplay' : '',
            'SectionDisplay' : '',
            'from' : request.POST.get('datepicker3'),
            'to' : request.POST.get('datepicker4'),
            'q' : list2,
        }
    if request.POST.get('TCPart') and not request.POST.get('TCDef'):
        defi = []
        list1 = []
        for x in qs6:
            qr = qs4.filter(TCName=x.id)
            q = qr.filter(TCDefArea=lo.id).count()
            if q != 0:
                list1.append(str(q))
        list2 = []
        for x in qs6:
            qr = qs4.filter(TCName=x.id)
            q = qr.filter(TCDefArea=lo.id).count()
            if q != 0:
                defi.append(str(x.TCName))
                p = qr.filter(TCDefArea=lo.id)
                for x in p:
                    list2.append(x)
                    print(p)
            else:
                pass
        context = {
            'DPC': defi,
            'time': currdate,
            'freq': list1,
            'RolStock' : 'TC',
            'PartDisplay' : lo.TCCArea,
            'SectionDisplay' : '',
            'from' : request.POST.get('datepicker3'),
            'to' : request.POST.get('datepicker4'),
            'q' : list2,
        }
    elif request.POST.get('TCDef') and not request.POST.get('TCPart'):
        defi = []
        list1 = []
        for x in qs6:
            qr = qs4.filter(TCName=x.id)
            q = qr.filter(TCSecArea=po.id).count()
            if q != 0:
                list1.append(str(q))
        list2 = []
        for x in qs6:
            qr = qs4.filter(TCName=x.id)
            q = qr.filter(TCSecArea=po.id).count()
            if q != 0:
                defi.append(str(x.TCName))
                p = qr.filter(TCSecArea=po.id)
                for x in p:
                    list2.append(x)
                    print(p)
            else:
                pass

        context = {
            'DPC': defi,
            'time': currdate,
            'freq': list1,
            'RolStock' : 'TC',
            'PartDisplay' : '',
            'SectionDisplay' : po.TCSec,
            'from' : request.POST.get('datepicker3'),
            'to' : request.POST.get('datepicker4'),
            'q' : list2,
        }
    elif request.POST.get('TCDef') and request.POST.get('TCPart'):
        defi = []
        list1 = []
        for x in qs6:
            qr = qs4.filter(TCName=x.id)
            q = qr.filter(TCSecArea=po.id).filter(TCDefArea=lo.id).count()
            if q != 0:
                list1.append(str(q))
        list2 = []
        for x in qs6:
            qr = qs4.filter(TCName=x.id)
            q = qr.filter(TCSecArea=po.id).filter(TCDefArea=lo.id).count()
            print(q)
            if q != 0:
                defi.append(str(x.TCName))
                p = qr.filter(TCSecArea=po.id).filter(TCDefArea=lo.id)
                for x in p:
                    list2.append(x)
                    print(p)
            else:
                pass
                print(list2)
        context = {
            'DPC': defi,
            'time': currdate,
            'freq': list1,
            'RolStock' : 'TC',
            'PartDisplay' : lo.TCCArea,
            'SectionDisplay' : po.TCSec,
            'from' : request.POST.get('datepicker3'),
            'to' : request.POST.get('datepicker4'),
            'q' : list2,
        }
    return render(request, 'charts/chartshome.html', context)


@login_required
def mcchart(request):
    currdate = date.today()
    print(request.POST.get('datepicker6'))
    qs6 = MC.objects.all().order_by('-POHDate').filter(POHDate__lt=request.POST.get('datepicker6'), POHDate__gt=request.POST.get('datepicker5'))
    qs4 = MCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=request.POST.get('datepicker6'), POHDate__gt=request.POST.get('datepicker5'))
    if request.POST.get('MCPart'):
        lo = MCArea.objects.get(MCArea=request.POST.get('MCPart'))
    if request.POST.get('MCDef'):
        po = MCSec.objects.get(MCSec=request.POST.get('MCDef'))
    if not request.POST.get('MCPart') and not request.POST.get('MCDef'):
        defi = []
        list1 = []
        for x in qs6:
            qr = qs4.filter(MCName=x.id)
            q = qr.count()
            if q != 0:
                list1.append(str(q))
        list2 = []
        for x in qs6:
            qr = qs4.filter(MCName=x.id)
            q = qr.count()
            print(q)
            if q != 0:
                defi.append(str(x.MCName))
                p = qr
                for x in p:
                    list2.append(x)
                    print(p)
            else:
                pass
                print(list2)
        context = {
            'DPC': defi,
            'time': currdate,
            'freq': list1,
            'RolStock' : 'MC',
            'PartDisplay' : '',
            'SectionDisplay' : '',
            'from' : request.POST.get('datepicker5'),
            'to' : request.POST.get('datepicker6'),
            'q' : list2,
        }
        
    if request.POST.get('MCPart') and not request.POST.get('MCDef'):
        defi = []
        list1 = []
        for x in qs6:
            qr = qs4.filter(MCName=x.id)
            q = qr.filter(MCDefArea=lo.id).count()
            if q != 0:
                list1.append(str(q))
        list2 = []
        for x in qs6:
            qr = qs4.filter(MCName=x.id)
            q = qr.filter(MCDefArea=lo.id).count()
            if q != 0:
                defi.append(str(x.MCName))
                p = qr.filter(MCDefArea=lo.id)
                for x in p:
                    list2.append(x)
                    print(p)
            else:
                pass
        context = {
            'DPC': defi,
            'time': currdate,
            'freq': list1,
            'RolStock' : 'MC',
            'PartDisplay' : lo.MCArea,
            'SectionDisplay' : '',
            'from' : request.POST.get('datepicker5'),
            'to' : request.POST.get('datepicker6'),
            'q' : list2,
        }
    elif request.POST.get('MCDef') and not request.POST.get('MCPart'):
        defi = []
        list1 = []
        for x in qs6:
            qr = qs4.filter(MCName=x.id)
            q = qr.filter(MCSecArea=po.id).count()
            if q != 0:
                list1.append(str(q))
        list2 = []
        for x in qs6:
            qr = qs4.filter(MCName=x.id)
            q = qr.filter(MCSecArea=po.id).count()
            if q != 0:
                defi.append(str(x.MCName))
                p = qr.filter(MCSecArea=po.id)
                for x in p:
                    list2.append(x)
                    print(p)
            else:
                pass

        context = {
            'DPC': defi,
            'time': currdate,
            'freq': list1,
            'RolStock' : 'MC',
            'PartDisplay' : '',
            'SectionDisplay' : po.MCSec,
            'from' : request.POST.get('datepicker5'),
            'to' : request.POST.get('datepicker6'),
            'q' : list2,
        }
    elif request.POST.get('MCDef') and request.POST.get('MCPart'):
        defi = []
        list1 = []
        for x in qs6:
            qr = qs4.filter(MCName=x.id)
            q = qr.filter(MCSecArea=po.id).filter(MCDefArea=lo.id).count()
            if q != 0:
                list1.append(str(q))
        list2 = []
        for x in qs6:
            qr = qs4.filter(MCName=x.id)
            q = qr.filter(MCSecArea=po.id).filter(MCDefArea=lo.id).count()
            print(q)
            if q != 0:
                defi.append(str(x.MCName))
                p = qr.filter(MCSecArea=po.id).filter(MCDefArea=lo.id)
                for x in p:
                    list2.append(x)
                    print(p)
            else:
                pass
                print(list2)
        context = {
            'DPC': defi,
            'time': currdate,
            'freq': list1,
            'RolStock' : 'MC',
            'PartDisplay' : lo.MCArea,
            'SectionDisplay' : po.MCSec,
            'from' : request.POST.get('datepicker5'),
            'to' : request.POST.get('datepicker6'),
            'q' : list2,
        }
    return render(request, 'charts/chartshome.html', context)
