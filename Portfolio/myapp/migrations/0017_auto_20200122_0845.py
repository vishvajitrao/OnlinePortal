# Generated by Django 2.2.7 on 2020-01-22 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_auto_20200122_0626'),
    ]

    operations = [
        migrations.CreateModel(
            name='TitleandTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('tagline', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='Category',
            field=models.CharField(choices=[('Python', 'Python Tutorial'), ('Python-tool', 'Python Coding Tool'), ('Python-external', 'Python External Module'), ('Flask', 'Flask Tutorial'), ('Python-built-in', 'Python Built-in Module'), ('Django', 'Django Tutorial')], default='Python Tutorial', max_length=20),
        ),
    ]
