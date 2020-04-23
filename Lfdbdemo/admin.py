import datetime
from django.db import models
from django.contrib import admin, messages
from Lfdbdemo.models import models
from Lfdbdemo.models import chang
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

# Register your models here.
@admin.register(chang)
class changAdmin(admin.ModelAdmin):
    list_display =('id', 'name', 'date_added')
    search_fields = ('name',)

@admin.register(bumen)
class bumenAdmin(admin.ModelAdmin):
    list_display=('id', 'bumen', 'date_added')
    search_fields =('name',)

@admin.register(title)
class titleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_added')
    search_fields = ('name',)





@admin.register(person)
class personAdmin(admin.ModelAdmin):

    list_display =('useid', 'name', 'chang','bumen', 'title','phone', 'date', 'number', 'shebao', 'beizhu', 'zhuangtai',
                   'update_time')
    search_fields =('name', 'number','cardnumber', 'phone',)
    list_per_page = 40
    list_filter = ('chang', 'zhuangtai', 'shebao')




    actions = ['update', 'custom_button']
    def custom_button(self, request, queryset):
        pass

    custom_button.short_description = '导出人员信息'
    custom_button.icon = 'fas fa-download'
    custom_button.type = 'success'
    custom_button.style = 'color:black;'




