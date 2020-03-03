# Generated by Django 2.2.7 on 2020-03-02 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_auto_20200302_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pmrp',
            field=models.IntegerField(default=0, verbose_name='Product M.R.P:- '),
        ),
        migrations.AddField(
            model_name='product',
            name='yousave',
            field=models.IntegerField(default=0, verbose_name='You Save:- '),
        ),
        migrations.AlterField(
            model_name='blog',
            name='Category',
            field=models.CharField(choices=[('Flask', 'Flask Tutorial'), ('Python-built-in', 'Python Built-in Module'), ('Python-external', 'Python External Module'), ('Django', 'Django Tutorial'), ('Python-tool', 'Python Coding Tool'), ('Python', 'Python Tutorial')], default='Python Tutorial', max_length=20),
        ),
    ]
