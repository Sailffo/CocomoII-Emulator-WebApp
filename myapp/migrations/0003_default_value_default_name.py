# Generated by Django 2.2.5 on 2019-12-16 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20191216_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='default_value',
            name='default_name',
            field=models.CharField(default='', max_length=20),
        ),
    ]