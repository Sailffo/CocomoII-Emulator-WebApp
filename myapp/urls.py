from django.urls import path
from . import views
import myapp

app_name = 'myapp'

urlpatterns = [
    path('',views.user_login,name = 'user_login'),#登录
    path('register/',views.register, name = 'register'),#注册
    path('index/',views.index,name = 'index'),#主页
    path('history/<str:user_name>/<int:history_id>',views.history,name = 'history'),#历史记录
    path('example/',views.example,name = 'example'),#新建模型
    path('logout/',views.user_logout,name = 'user_logout'),#退出登录
    path('parameter/',views.parameter,name = 'parameter'),#相关参考
    path('self_information/',views.self_information,name = 'self_information'),#个人信息
    path('report/',views.report,name = 'report'),#个人信息
]
