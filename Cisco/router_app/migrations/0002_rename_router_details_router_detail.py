# Generated by Django 4.0.1 on 2022-02-14 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('router_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='router_details',
            new_name='router_detail',
        ),
    ]