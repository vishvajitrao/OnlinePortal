# Generated by Django 2.2.7 on 2019-12-05 07:19

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20191205_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Category',
            field=models.CharField(choices=[('Python-external', 'Python External Module'), ('Flask', 'Flask Tutorial'), ('Python', 'Python Tutorial'), ('Django', 'Django Tutorial'), ('Python-built-in', 'Python Built-in Module'), ('Python-tool', 'Python Coding Tool')], default='Python Tutorial', max_length=20),
        ),
        migrations.AlterField(
            model_name='headerad',
            name='Header_Ad',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
