# Generated by Django 2.2.7 on 2020-01-08 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20200108_0459'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siteicon', models.FileField(blank=True, null=True, upload_to='icons', verbose_name='Website Icon')),
            ],
        ),
        migrations.RemoveField(
            model_name='logo',
            name='siteicon',
        ),
        migrations.AlterField(
            model_name='blog',
            name='Category',
            field=models.CharField(choices=[('Python-tool', 'Python Coding Tool'), ('Python-built-in', 'Python Built-in Module'), ('Flask', 'Flask Tutorial'), ('Django', 'Django Tutorial'), ('Python', 'Python Tutorial'), ('Python-external', 'Python External Module')], default='Python Tutorial', max_length=20),
        ),
    ]
