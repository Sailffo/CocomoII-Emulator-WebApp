# Generated by Django 2.0.3 on 2019-12-16 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(db_column='模型名', max_length=20, verbose_name='模型名')),
                ('model_A', models.FloatField(default='2.94', max_length=20, verbose_name='A')),
                ('SIZE', models.FloatField(max_length=20, null=True, verbose_name='代码行数(千行)')),
                ('PREC', models.FloatField(default=None, max_length=20, verbose_name='前例')),
                ('FLEX', models.FloatField(default=None, max_length=20, verbose_name='开发灵活性')),
                ('RESL', models.FloatField(default=None, max_length=20, verbose_name='体系结构和风险控制')),
                ('TEAM', models.FloatField(default=None, max_length=20, verbose_name='项目成员合作程度')),
                ('PMAT', models.FloatField(default=None, max_length=20, verbose_name='过程成熟度')),
                ('SCED', models.FloatField(default=None, max_length=20, verbose_name='进度压力')),
                ('TDEV', models.FloatField(max_length=20, null=True, verbose_name='项目进度')),
                ('PM', models.FloatField(max_length=20, null=True, verbose_name='工作量')),
                ('last_edit', models.DateTimeField(auto_now=True, verbose_name='上一次修改')),
                ('isdelete', models.BooleanField(db_column='是否删除', default=False)),
                ('lastTime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'datamodels',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='User_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(db_column='名字', default='', max_length=20, verbose_name='名字')),
                ('user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'db_table': 'users',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='datamodel',
            name='model_user',
            field=models.ForeignKey(db_column='用户', on_delete=django.db.models.deletion.CASCADE, related_name='user_models', to='myapp.User_name', verbose_name='用户'),
        ),
    ]
