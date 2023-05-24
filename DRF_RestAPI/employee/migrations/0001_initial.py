# Generated by Django 4.2.1 on 2023-05-24 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=30)),
                ('employee_post', models.CharField(max_length=30)),
                ('employee_email', models.EmailField(max_length=30)),
                ('employee_mobile', models.CharField(max_length=10)),
                ('Date_of_joining', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]