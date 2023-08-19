from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import DPC, TC,MC, DPCArea, DPCRemark,TCArea, TCRemark, MCArea, MCRemark, Shed, Shop, DPCSec, TCSec, MCSec, Status
from import_export import resources
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget


# Register your models here


class DPCRemarkResource(resources.ModelResource):
    DPCName_id = Field(
        column_name='DPCName_id',
        attribute='DPCName_id',
        widget=ForeignKeyWidget(DPC, 'DPCName'))

    class Meta:
        model = DPCRemark

class DPCRemarkAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (['DPCName'])
    resources_class = DPCRemarkResource

admin.site.register(DPC)
admin.site.register(TC)
admin.site.register(MC)
admin.site.register(DPCArea)
admin.site.register(DPCSec)
admin.site.register(DPCRemark, DPCRemarkAdmin)
admin.site.register(TCArea)
admin.site.register(TCSec)
admin.site.register(TCRemark)
admin.site.register(MCArea)
admin.site.register(MCSec)
admin.site.register(MCRemark)
admin.site.register(Shed)
admin.site.register(Shop)
admin.site.register(Status)
