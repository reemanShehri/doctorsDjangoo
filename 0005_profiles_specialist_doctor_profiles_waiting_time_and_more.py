# Generated by Django 5.1.1 on 2024-12-30 22:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profiles_slug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='Specialist_doctor',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='تخصص الطبيب'),
        ),
        migrations.AddField(
            model_name='profiles',
            name='Waiting_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='مدة الانتظار'),
        ),
        migrations.AddField(
            model_name='profiles',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='العنوان'),
        ),
        migrations.AddField(
            model_name='profiles',
            name='address_detail',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='تفاصيل العنوان'),
        ),
        migrations.AddField(
            model_name='profiles',
            name='doctor',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='الطبيب'),
        ),
        migrations.AddField(
            model_name='profiles',
            name='number_phone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='رقم الهاتف'),
        ),
        migrations.AddField(
            model_name='profiles',
            name='subtitle',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='عنوان'),
        ),
        migrations.AddField(
            model_name='profiles',
            name='working_hours',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='عدد ساعات العمل'),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile', verbose_name=' الصورة '),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='name',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='الاسم'),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='السعر'),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='who_i',
            field=models.TextField(blank=True, max_length=250, null=True, verbose_name='من انا'),
        ),
    ]
