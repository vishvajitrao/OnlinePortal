# Generated by Django 2.2.7 on 2020-01-06 09:53

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20200106_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='Header_Ad',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ads',
            name='article_one',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ads',
            name='article_three',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ads',
            name='article_two',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ads',
            name='bottom',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ads',
            name='sidebar_one',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ads',
            name='sidebar_two',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='Category',
            field=models.CharField(choices=[('Python-built-in', 'Python Built-in Module'), ('Python', 'Python Tutorial'), ('Python-tool', 'Python Coding Tool'), ('Python-external', 'Python External Module'), ('Flask', 'Flask Tutorial'), ('Django', 'Django Tutorial')], default='Python Tutorial', max_length=20),
        ),
    ]
