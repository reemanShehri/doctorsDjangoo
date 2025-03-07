# Generated by Django 5.1.1 on 2024-12-26 21:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='الاسم:')),
                ('who_i', models.CharField(max_length=250, verbose_name='من أنا :')),
                ('price', models.IntegerField(verbose_name='سعر الكشف:')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='')),
            ],
            options={
                'verbose_name': 'Profiles',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
