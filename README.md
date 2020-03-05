# CocomoII-Emulator-WebApp
cocomoII成本预测web应用

采用django框架，版本2.0.3
数据库采用django自带sqlite3

用户新建的模型会依赖于管理员设置的参数值，因而在初始化数据库前需要将DataModel注释掉，即models文件中的28-83行，admin文件中的6-26行，

注释掉之后再执行python manage.py makemigrations和python manage.py migrate进行数据库迁移,

迁移完数据库再创建超级用户python manage.py createsuperuser在后台新增参数值default_value,

所包含的参数值为[

        'prec', 'flex', 'resl', 'team', 'pmat', 'rely', 'data', 'docu', 'cplx', 'ruse', 'time',
        
        'stor', 'pvol', 'acap', 'aexp', 'pcap', 'pexp', 'ltex', 'pcon', 'tool', 'sced', 'site',
        
    ]
每个参数均有5个值very low,low,normal,high,very high,extra high,

设置完成后，取消之前的代码注释，重新执行数据库迁移即完成系统搭建。

有任何问题请私信邮箱sailffo@qq.com
