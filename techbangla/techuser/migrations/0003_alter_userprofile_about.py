# Generated by Django 3.2 on 2021-07-14 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techuser', '0002_auto_20210714_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='about',
            field=models.TextField(blank=True, verbose_name='About Yourself'),
        ),
    ]
