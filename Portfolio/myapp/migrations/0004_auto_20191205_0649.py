# Generated by Django 2.2.7 on 2019-12-05 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20191204_0952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Headerad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ad_name', models.CharField(max_length=20)),
                ('Header_Ad', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='Category',
            field=models.CharField(choices=[('Python-tool', 'Python Coding Tool'), ('Flask', 'Flask Tutorial'), ('Python', 'Python Tutorial'), ('Python-built-in', 'Python Built-in Module'), ('Django', 'Django Tutorial'), ('Python-external', 'Python External Module')], default='Python Tutorial', max_length=20),
        ),
    ]
