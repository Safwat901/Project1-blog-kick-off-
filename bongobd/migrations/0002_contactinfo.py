# Generated by Django 3.2.4 on 2021-06-22 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bongobd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('cemail', models.EmailField(max_length=50)),
                ('cquery', models.TextField(max_length=1000)),
            ],
        ),
    ]
