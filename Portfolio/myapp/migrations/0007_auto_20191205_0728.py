# Generated by Django 2.2.7 on 2019-12-05 07:28

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20191205_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Category',
            field=models.CharField(choices=[('Python-built-in', 'Python Built-in Module'), ('Django', 'Django Tutorial'), ('Python-tool', 'Python Coding Tool'), ('Flask', 'Flask Tutorial'), ('Python-external', 'Python External Module'), ('Python', 'Python Tutorial')], default='Python Tutorial', max_length=20),
        ),
        migrations.AlterField(
            model_name='headerad',
            name='Header_Ad',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
