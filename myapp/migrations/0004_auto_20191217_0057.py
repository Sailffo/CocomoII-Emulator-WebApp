# Generated by Django 2.2.5 on 2019-12-16 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_default_value_default_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='datamodel',
            name='ACAP',
            field=models.FloatField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='datamodel',
            name='AEXP',
            field=models.FloatField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='datamodel',
            name='CPLX',
            field=models.FloatField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='datamodel',
            name='DATA',
            field=models.FloatField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='datamodel',
            name='DOCU',
            field=models.FloatField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='datamodel',
            name='LTEX',
            field=models.FloatField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='datamodel',
            name='PCAP',
            field=models.FloatField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='datamodel',
            name='PCON',
            field=models.FloatField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='datamodel',
            name='PEXP',
            field=models.FloatField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='datamodel',
            name='PVOL',
            field=models.FloatField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='datamodel',
            name='RELY',
            field=models.FloatField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='datamodel',
            name='RUSE',
            field=models.FloatField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='datamodel',
            name='SITE',
            field=models.FloatField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='datamodel',
            name='STOR',
            field=models.FloatField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='datamodel',
            name='TIME',
            field=models.FloatField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='datamodel',
            name='TOOL',
            field=models.FloatField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='FLEX',
            field=models.FloatField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='PMAT',
            field=models.FloatField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='PREC',
            field=models.FloatField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='RESL',
            field=models.FloatField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='SCED',
            field=models.FloatField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='SIZE',
            field=models.FloatField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='TEAM',
            field=models.FloatField(default=None, max_length=20),
        ),
    ]