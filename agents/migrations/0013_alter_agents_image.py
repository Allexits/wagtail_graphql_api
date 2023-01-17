# Generated by Django 3.2.16 on 2022-12-26 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('agents', '0012_alter_agentsconnection_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agents',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]