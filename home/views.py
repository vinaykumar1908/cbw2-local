
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render
import datetime
from datetime import timedelta, date
# Create your views here.
from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#from sidingz import models as ZM
from django.urls import reverse_lazy
from django.db import models
import math
from datetime import date, datetime

from itertools import filterfalse
#from .forms import registerStockRecievedForm, registerStockDispatchROHform, registerStockDispatchSicklineform, registerStockDispatchedYardform, registerStockDispatchedTrainDutyform
from django.utils import timezone
# Create your views here.
from django.contrib.auth.decorators import login_required

from django.db.models import Avg, Sum
from defi.models import DPC, TC, MC, DPCArea, DPCRemark, MCArea, MCRemark, TCArea, TCRemark


@login_required
def homeView(request):
    qs = DPC.objects.all().count()
    qs2 = TC.objects.all().count()
    qs3 = MC.objects.all().count()
    qs4 = DPCRemark.objects.all().count()
    qs5 = TCRemark.objects.all().count()
    qs6 = MCRemark.objects.all().count()
    qs7 = DPCArea.objects.all().count()
    qs8 = TCArea.objects.all().count()
    qs9 = MCArea.objects.all().count()
        

    #qs1 = RM.Rake.objects.all()

    timerightnow = timezone.now()
    today = date.today()
    yesterday = date.today() - timedelta(days=1)

    #qs2 = CCDetails.objects.filter(Date__gt=today, Date__lt=timezone.now())
    print(qs)
    #qs3 = STRDetails.objects.filter(Date__gt=today, Date__lt=timezone.now())
    #qs4 = CCDetails.objects.filter(Date__gt=yesterday, Date__lt=today)
    #qs5 = STRDetails.objects.filter(Date__gt=yesterday, Date__lt=today)
    #qs6 = CCDetails.objects.filter(Date__gt=yesterday, Date__lt=today)
    #qs6 = qs2.filter(PostExamDetails=True)
    #qs7 = STRDetails.objects.filter(Date__gt=yesterday, Date__lt=today)
    #qs7 = qs3.filter(PostExamDetails=True)
    #qs8 = CCDetails.objects.filter(Date__gt=yesterday, Date__lt=today).filter(PostExamDetails=True)
    #qs9 = STRDetails.objects.filter(Date__gt=yesterday, Date__lt=today).filter(PostExamDetails=True)
    #a = qs2.aggregate(Avg('MechanicalDetention'))
    #b = qs2.aggregate(Sum('TrafficDetention'))


    context = {
        'a' : qs,
        'b' : qs2,
        'c' : qs3,
        'd' : qs4,
        'e' : qs5,
        'f' : qs6,
        'g' : today,
        'h' : yesterday,
        'i' : qs7,
        'j' : qs8,
        'k' : qs9,
        
        'time' : timerightnow,
        
        
    }
    return render(request, 'home/home.html', context)

