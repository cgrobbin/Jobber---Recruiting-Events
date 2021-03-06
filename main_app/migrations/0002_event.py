# Generated by Django 3.1.7 on 2021-03-16 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=25)),
                ('speakers', models.CharField(max_length=250)),
                ('focus', models.CharField(choices=[('T', 'Tech'), ('M', 'Marketing'), ('C', 'Content Creation')], default='T', max_length=1)),
                ('description', models.TextField()),
                ('url', models.CharField(default='https://us05web.zoom.us/j/7915630422?pwd=Q2hnV2NnUEdFVTNYNUJRTWtHdDlzZz09', max_length=250)),
            ],
        ),
    ]
