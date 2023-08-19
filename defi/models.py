from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

class Shop(models.Model):
    ShopName = models.CharField(max_length=100, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='shopauth')
    def __str__(self):
        return self.ShopName
    
class Shed(models.Model):
    ShedName = models.CharField(max_length=100, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='shedauth')
    def __str__(self):
        return self.ShedName


class Status(models.Model):
    Status = models.CharField(max_length=100, blank=True, null=True, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.Status
    

class DPC(models.Model):
    DPCName = models.CharField(max_length=100, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    POHDate = models.DateField(null=True, blank=True)
    Shop = models.ForeignKey(Shop, on_delete=models.CASCADE,null=True, related_name='DPCShop')
    Shed = models.ForeignKey(Shed, on_delete=models.CASCADE,null=True, related_name='DPCShed')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='dpcauth')
    def __str__(self):
        return self.DPCName

class TC(models.Model):
    TCName = models.CharField(max_length=100, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    POHDate = models.DateField(null=True, blank=True)
    Shop = models.ForeignKey(Shop, on_delete=models.CASCADE,null=True, related_name='TCShop')
    Shed = models.ForeignKey(Shed, on_delete=models.CASCADE,null=True, related_name='TCShed')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='tcauth')
    
    def __str__(self):
        return self.TCName

class MC(models.Model):
    MCName = models.CharField(max_length=100, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    POHDate = models.DateField(null=True, blank=True)
    Shop = models.ForeignKey(Shop, on_delete=models.CASCADE,null=True, related_name='MCShop')
    Shed = models.ForeignKey(Shed, on_delete=models.CASCADE,null=True, related_name='MCShed')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='mcauth')
    
    def __str__(self):
        return self.MCName

class DPCArea(models.Model):
    DPCArea = models.CharField(max_length=100, blank=True, null=True, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.DPCArea
    
class DPCSec(models.Model):
    DPCSec = models.CharField(max_length=100, blank=True, null=True, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.DPCSec

class DPCRemark(models.Model):
    DPCName = models.ForeignKey(DPC, on_delete=models.CASCADE, related_name='DPCName1')
    Date = models.DateTimeField(default=timezone.now)
    POHDate = models.DateField(null=True, blank=True)
    DPCDefArea = models.ForeignKey(DPCArea, on_delete=models.CASCADE, related_name='DPCArea1')
    DPCDef = models.CharField(max_length=500, blank=True, null=True)
    DPCSecArea = models.ForeignKey(DPCSec, on_delete=models.CASCADE,null=True, related_name='DPCSecArea1')
    DPCStatus = models.ForeignKey(Status, on_delete=models.CASCADE,null=True, related_name='DPCStatus')
    def __str__(self):
        return self.DPCName.DPCName

class TCArea(models.Model):
    TCCArea = models.CharField(max_length=100, blank=True, null=True, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.TCCArea


class TCSec(models.Model):
    TCSec = models.CharField(max_length=100, blank=True, null=True, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.TCSec

class TCRemark(models.Model):
    Date = models.DateTimeField(default=timezone.now)
    TCName = models.ForeignKey(TC, on_delete=models.CASCADE, related_name='TCName1')
    POHDate = models.DateField(null=True, blank=True)
    TCDefArea = models.ForeignKey(TCArea, on_delete=models.CASCADE, related_name='TCArea1')
    TCDef = models.CharField(max_length=500, blank=True, null=True)
    TCSecArea = models.ForeignKey(TCSec, on_delete=models.CASCADE,null=True, related_name='TCSecArea1')
    TCStatus = models.ForeignKey(Status, on_delete=models.CASCADE,null=True, related_name='TCStatus')
    def __str__(self):
        return self.TCName.TCName

class MCArea(models.Model):
    MCArea = models.CharField(max_length=100, blank=True, null=True, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.MCArea
    

class MCSec(models.Model):
    MCSec = models.CharField(max_length=100, blank=True, null=True, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.MCSec

class MCRemark(models.Model):
    Date = models.DateTimeField(default=timezone.now)
    MCName = models.ForeignKey(MC, on_delete=models.CASCADE, related_name='MCName1')
    POHDate = models.DateField(null=True, blank=True)
    MCDefArea = models.ForeignKey(MCArea, on_delete=models.CASCADE, related_name='MCArea1')
    MCSecArea = models.ForeignKey(MCSec, on_delete=models.CASCADE,null=True, related_name='MCSecArea1')
    MCStatus = models.ForeignKey(Status, on_delete=models.CASCADE,null=True, related_name='MCStatus')
    MCDef = models.CharField(max_length=500, blank=True, null=True)
    def __str__(self):
        return self.MCName.MCName


