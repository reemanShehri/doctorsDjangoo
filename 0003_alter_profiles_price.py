# Generated by Django 5.1.1 on 2024-12-29 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profiles_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='سعر الكشف:'),
        ),
    ]
