# Generated by Django 2.2.7 on 2020-01-06 10:12

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20200106_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True)),
                ('slug', models.SlugField(max_length=20, unique=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='Category',
            field=models.CharField(choices=[('Python-built-in', 'Python Built-in Module'), ('Python-tool', 'Python Coding Tool'), ('Flask', 'Flask Tutorial'), ('Django', 'Django Tutorial'), ('Python-external', 'Python External Module'), ('Python', 'Python Tutorial')], default='Python Tutorial', max_length=20),
        ),
    ]
