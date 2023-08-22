from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from defi.models import DPC, TC, MC, DPCArea, DPCRemark, TCArea, TCRemark, MCArea, MCRemark, Shop, Shed, DPCSec, TCSec, MCSec, Status
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

def rakeView(request):
    context = {
            #'messages': message,
            """ 'object': p,
            'q' : q,
            'DPC': defi,
            'freq': list1 ,
 """            }
    return render(request, 'rake/rakehome.html')