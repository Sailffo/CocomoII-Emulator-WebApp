# Generated by Django 2.2.5 on 2019-12-16 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Default_value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('very_low', models.FloatField(max_length=20)),
                ('low', models.FloatField(max_length=20)),
                ('normal', models.FloatField(max_length=20)),
                ('high', models.FloatField(max_length=20)),
                ('very_high', models.FloatField(max_length=20)),
                ('extra_high', models.FloatField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='datamodel',
            name='model_A',
        ),
    ]