# Generated by Django 2.0.3 on 2018-03-25 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('st_web', '0004_tutorial_detail_submitted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorial_detail',
            name='submitted',
        ),
    ]