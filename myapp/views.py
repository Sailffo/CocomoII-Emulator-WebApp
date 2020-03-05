import codecs
import math
import os

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import unicodecsv as ucsv

from myapp.models import *

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['user_name'],
                            password=request.POST['pwd'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/index/")

    return render(request,'myapp/login.html')

def register(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        name = request.POST['name']
        password = request.POST['pwd']
        user = User(username=user_name)
        user.set_password(password)
        user.save()
        temp = User_name(user=user,user_name=name)
        temp.save()
        return HttpResponseRedirect("/")
    return render(request,'myapp/register.html')


@login_required(login_url = 'myapp:login')
def index(request):
    error = ''
    name = request.user.user_name
    models = DataModel.objects.filter(model_user=name,isdelete=False).all().order_by("-last_edit")
    if not len(models):
        error = '无历史记录'
    if request.method == 'POST':
        model_id = request.POST['shanchu']
        model = DataModel.objects.get(id=model_id)
        model.isdelete = True
        model.save()
        return redirect("/index/")
    return render(request,'myapp/index.html',{"name":name,'history':models,'error':error})

@login_required(login_url = 'myapp:login')
def history(request,user_name,history_id):
    name = request.user.user_name
    model = DataModel.objects.get(id = history_id)
    drivers = {
        'prec': 0,
        'flex': 0, 'resl': 0,
        'team': 0, 'pmat': 0,
        'rely': 0, 'data': 0,
        'docu': 0, 'cplx': 0,
        'ruse': 0, 'time': 0,
        'stor': 0, 'pvol': 0,
        'acap': 0, 'aexp': 0,
        'pcap': 0, 'pexp': 0,
        'ltex': 0, 'pcon': 0,
        'tool': 0, 'sced': 0,
        'site': 0}
    if request.method == 'POST':
        modelName = request.POST['model_name']
        size = request.POST['size']
        for key in drivers:
            id = request.POST[key]
            if (id == '非常低'):
                drivers[key] = '非常低'
            elif (id == '低'):
                drivers[key] = '低'
            elif (id == '正常'):
                drivers[key] = '正常'
            elif (id == '高'):
                drivers[key] = '高'
            elif (id == '非常高'):
                drivers[key] = '非常高'
            elif (id == '超高'):
                drivers[key] = '超高'

        model.model_name = modelName
        model.PREC = drivers['prec']
        model.FLEX = drivers['flex']
        model.RESL = drivers['resl']
        model.TEAM = drivers['team']
        model.PMAT = drivers['pmat']
        model.RELY = drivers['rely']
        model.DATA = drivers['data']
        model.DOCU = drivers['docu']
        model.CPLX = drivers['cplx']
        model.RUSE = drivers['ruse']
        model.TIME = drivers['time']
        model.STOR = drivers['stor']
        model.PVOL = drivers['pvol']
        model.ACAP = drivers['acap']
        model.AEXP = drivers['aexp']
        model.PCAP = drivers['pcap']
        model.PEXP = drivers['pexp']
        model.LTEX = drivers['ltex']
        model.PCON = drivers['pcon']
        model.TOOL = drivers['tool']
        model.SCED = drivers['sced']
        model.SITE = drivers['site']
        model.SIZE = size
        model.save()
        first = DataModel.objects.filter(model_name=modelName, model_user=request.user.user_name).order_by("-last_edit").first()
        id = first.id
        caculation(modelName,model.model_user,id)
        return redirect("/index/")
    return render(request,'myapp/history.html',{"model":model,"name":name})


def user_logout(request):
    logout(request)
    return redirect("/")

@login_required(login_url = 'myapp:login')
def example(request):
    name = request.user.user_name
    drivers = {
        'prec':0,
        'flex':0,'resl':0,
        'team':0,'pmat':0,
        'rely':0,'data':0,
        'docu':0,'cplx':0,
        'ruse':0,'time':0,
        'stor':0,'pvol':0,
        'acap':0,'aexp':0,
        'pcap':0,'pexp':0,
        'ltex':0,'pcon':0,
        'tool':0,'sced':0,
        'site':0}
    if request.method == 'POST':
        modelName = request.POST['model_name']
        size = request.POST['size']
        for key in drivers:
            id = request.POST[key]
            if(id == '非常低'):
                drivers[key] = '非常低'
            elif(id == '低'):
                drivers[key] = '低'
            elif (id == '正常'):
                drivers[key] = '正常'
            elif (id == '高'):
                drivers[key] = '高'
            elif (id == '非常高'):
                drivers[key] = '高'
            elif (id == '超高'):
                drivers[key] = '超高'

        temp = DataModel(model_user=request.user.user_name,SIZE=size,model_name=modelName,PREC=drivers['prec'],FLEX=drivers['flex'],
                         RESL=drivers['resl'],TEAM=drivers['team'],PMAT=drivers['pmat'],RELY=drivers['rely'],DATA=drivers['data'],DOCU=drivers['docu'],
                         CPLX=drivers['cplx'],RUSE=drivers['ruse'],TIME=drivers['time'],STOR=drivers['stor'],PVOL=drivers['pvol'],ACAP=drivers['acap'],
                         AEXP=drivers['aexp'],PCAP=drivers['pcap'],PEXP=drivers['pexp'],LTEX=drivers['ltex'],PCON=drivers['pcon'],TOOL=drivers['tool'],
                         SCED=drivers['sced'],SITE=drivers['site'])
        temp.save()
        first = DataModel.objects.filter(model_name=modelName,model_user=request.user.user_name).order_by("-last_edit").first()
        id = first.id
        caculation(modelName,request.user.user_name,id)
        return redirect("/index/")
    return render(request,'myapp/examples.html',{"name":name})

def caculation(name,user_name,id):
    A = 2.94
    model = DataModel.objects.get(model_name=name,model_user=user_name,id = id)
    B = 0.91 + 0.01 * (model.get_PREC_display() + model.get_FLEX_display() + model.get_RESL_display() + model.get_TEAM_display() + model.get_PMAT_display())
    C = model.get_RELY_display() * model.get_DATA_display() * model.get_DOCU_display() * model.get_CPLX_display() * model.get_RUSE_display() * model.get_TIME_display() * \
        model.get_STOR_display() * model.get_PVOL_display() * model.get_ACAP_display() * model.get_AEXP_display() * model.get_PCAP_display() * model.get_PEXP_display() * \
        model.get_LTEX_display() * model.get_PCON_display() * model.get_TOOL_display() * model.get_SCED_display() * model.get_SITE_display()
    pm = A * math.pow(float(model.SIZE), B) * C
    tdev = 3.67 * math.pow(pm, 0.28 + 0.2 * (B - 0.91)) * model.get_SCED_display() / 10000
    model.PM = pm
    model.TDEV = tdev
    model.save()


@login_required(login_url = 'myapp:login')
def parameter(request):
    name = request.user.user_name
    models = Default_value.objects.all()
    return render(request,'myapp/parameter.html',{"name":name,'history':models})

@login_required(login_url = 'myapp:login')
def self_information(request):
    name = request.user
    a = User_name.objects.all().get(user=name)
    return render(request,'myapp/self_information.html',{"user":a,"t":name})

@login_required(login_url = 'myapp:login')
def report(request):
    path = 'C:\\Users\\Administrator\\Documents\\PycharmProjects\\Economics\\static\\'
    name2 = request.user.user_name.user_name
    global row
    table = {}
    selcted = []
    name = request.user.user_name
    models = DataModel.objects.filter(model_user=name,isdelete=False).all().order_by("-last_edit")
    if request.method == 'POST':
        for model in models:
            x = request.POST[str(model.id)]
            table[model.id] = x
        for key in table:
            if table[key] == '1':
                selcted.append(DataModel.objects.get(id=key))
        header = ['MODELNAME','SIZE','PM','TDEV',
            'PREC', 'FLEX', 'RESL', 'TEAM', 'PMAT', 'RELY', 'DATA', 'DOCU', 'CPLX', 'RUSE', 'TIME',
            'STOR', 'PVOL', 'ACAP', 'AEXP', 'PCAP', 'PEXP', 'LTEX', 'PCON', 'TOOL', 'SCED', 'SITE',
        ]
        rows = []
        for file in selcted:
            row = []
            row.append(file.model_name)
            row.append(str(file.SIZE))
            row.append(str(file.PM))
            row.append(str(file.TDEV))
            row.append(str(file.get_PREC_display()))
            row.append(str(file.get_FLEX_display()))
            row.append(str(file.get_RESL_display()))
            row.append(str(file.get_TEAM_display()))
            row.append(str(file.get_PMAT_display()))
            row.append(str(file.get_RELY_display()))
            row.append(str(file.get_DATA_display()))
            row.append(str(file.get_DOCU_display()))
            row.append(str(file.get_CPLX_display()))
            row.append(str(file.get_RUSE_display()))
            row.append(str(file.get_TIME_display()))
            row.append(str(file.get_STOR_display()))
            row.append(str(file.get_PVOL_display()))
            row.append(str(file.get_ACAP_display()))
            row.append(str(file.get_AEXP_display()))
            row.append(str(file.get_PCAP_display()))
            row.append(str(file.get_PEXP_display()))
            row.append(str(file.get_LTEX_display()))
            row.append(str(file.get_PCON_display()))
            row.append(str(file.get_TOOL_display()))
            row.append(str(file.get_SCED_display()))
            row.append(str(file.get_SITE_display()))
            rows.append(row)
        if not os.path.exists(path+str(name)+str(name2)):
            os.mkdir(path+str(name)+str(name2))
        with open(path+str(name)+str(name2)+'\\cocomoII.csv','wb') as csvfile:
            w = ucsv.writer(csvfile,encoding='utf_8_sig')
            w.writerow(header)
            w.writerows(rows)
    return render(request,'myapp/report.html',{"name":name,'history':models,"name1":str(name),"name2":str(name2)})


