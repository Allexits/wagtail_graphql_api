# Generated by Django 3.2.16 on 2022-12-22 16:20

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0008_alter_agentspage_agents'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agentspage',
            name='agents',
        ),
        migrations.AddField(
            model_name='agents',
            name='parent',
            field=modelcluster.fields.ParentalManyToManyField(related_name='agent', to='agents.AgentsPage'),
        ),
        migrations.DeleteModel(
            name='AgentsConnection',
        ),
    ]
