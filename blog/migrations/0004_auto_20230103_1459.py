# Generated by Django 3.2.16 on 2023-01-03 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpage_first_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='first_parent',
        ),
        migrations.AddField(
            model_name='blogdetailpage',
            name='first_parent',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
