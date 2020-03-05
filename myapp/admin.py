from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class DataModelInline(admin.TabularInline):
    model = DataModel
    can_delete = False
    verbose_name_plural = "模型"


class DataModelInfo(admin.TabularInline):
    model = DataModel
    extra = 3

@admin.register(DataModel)
class DataModelAdmin(admin.ModelAdmin):
    list_display =['last_edit','id','model_user','model_name','PREC','FLEX','RESL','TEAM','PMAT','SCED','TDEV','PM','isdelete']

    class Meta:
        ordering = ['last_edit']

@admin.register(User_name)
class User_nameAdmin(admin.ModelAdmin):
    inlines = [DataModelInfo]
    list_display = ['pk','user_name']

@admin.register(Default_value)
class User_nameAdmin(admin.ModelAdmin):
    list_display = ['pk','default_name','very_low','low','normal','high','very_high','extra_high']
