# Generated by Django 3.2.9 on 2022-03-01 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Название')),
                ('text', models.TextField(verbose_name='Описание')),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
    ]
