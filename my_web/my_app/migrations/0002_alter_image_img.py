# Generated by Django 3.2.9 on 2022-03-01 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
