import datetime

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# 用户模型
class User_name(models.Model):
    user = models.OneToOneField(User,default='',on_delete=models.CASCADE,verbose_name='用户')
    user_name = models.CharField(max_length=20,db_column='名字',verbose_name='名字',default='')
    #元选项
    class Meta:
        db_table = 'users'
        ordering = ['id']

# 所有的参数默认值
class Default_value(models.Model):
    default_name = models.CharField(max_length=20,default='')
    very_low = models.FloatField(max_length=20)
    low = models.FloatField(max_length=20)
    normal = models.FloatField(max_length=20)
    high = models.FloatField(max_length=20)
    very_high = models.FloatField(max_length=20)
    extra_high = models.FloatField(max_length=20)


# 用户创建的计算模型
class DataModel(models.Model):
    drivers = [
        'prec', 'flex', 'resl', 'team', 'pmat', 'rely', 'data', 'docu', 'cplx', 'ruse', 'time',
        'stor', 'pvol', 'acap', 'aexp', 'pcap', 'pexp', 'ltex', 'pcon', 'tool', 'sced', 'site',
    ]
    choices_list = []
    for key in drivers:
        defalt_value = Default_value.objects.get(default_name=key.upper())
        choices = (
            ('非常低',defalt_value.very_low),
            ('低',defalt_value.low),
            ('正常',defalt_value.normal),
            ('高',defalt_value.high),
            ('非常高',defalt_value.very_high),
            ('超高',defalt_value.extra_high),
        )
        choices_list.append(choices)
    model_user = models.ForeignKey('User_name',on_delete=models.CASCADE,related_name='user_models',verbose_name='用户',db_column='用户')
    model_name = models.CharField(max_length=20,db_column='模型名',verbose_name='模型名')
    SIZE = models.CharField(max_length=20,null=True)
    PREC = models.CharField(max_length=20,default=None,choices=choices_list[0])
    FLEX = models.CharField(max_length=20,default=None,choices=choices_list[1])
    RESL = models.CharField(max_length=20,default=None,choices=choices_list[2])
    TEAM = models.CharField(max_length=20,default=None,choices=choices_list[3])
    PMAT = models.CharField(max_length=20,default=None,choices=choices_list[4])
    RELY = models.CharField(max_length=20,default=None,choices=choices_list[5])
    DATA = models.CharField(max_length=20,default=None,choices=choices_list[6])
    DOCU = models.CharField(max_length=20,default=None,choices=choices_list[7])
    CPLX = models.CharField(max_length=20,default=None,choices=choices_list[8])
    RUSE = models.CharField(max_length=20,default=None,choices=choices_list[9])
    TIME = models.CharField(max_length=20,default=None,choices=choices_list[10])
    STOR = models.CharField(max_length=20,default=None,choices=choices_list[11])
    PVOL = models.CharField(max_length=20,default=None,choices=choices_list[12])
    ACAP = models.CharField(max_length=20,default=None,choices=choices_list[13])
    AEXP = models.CharField(max_length=20,default=None,choices=choices_list[14])
    PCAP = models.CharField(max_length=20,default=None,choices=choices_list[15])
    PEXP = models.CharField(max_length=20,default=None,choices=choices_list[16])
    LTEX = models.CharField(max_length=20,default=None,choices=choices_list[17])
    PCON = models.CharField(max_length=20,default=None,choices=choices_list[18])
    TOOL = models.CharField(max_length=20,default=None,choices=choices_list[19])
    SCED = models.CharField(max_length=20,default=None,choices=choices_list[20])
    SITE = models.CharField(max_length=20,default=None,choices=choices_list[21])


    TDEV = models.FloatField(max_length=20,verbose_name='项目进度',null=True)
    PM = models.FloatField(max_length=20,null=True,verbose_name='工作量')
    last_edit = models.DateTimeField(verbose_name='上一次修改',auto_now=True)
    isdelete =models.BooleanField(db_column='是否删除',default=False)

    def __str__(self):
        return "%s"%(self.model_name)
    lastTime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'datamodels'
        ordering = ['id']

