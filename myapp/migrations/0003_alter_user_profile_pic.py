# Generated by Django 3.2 on 2021-04-21 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_passid_pass_charges'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Profile_pic',
            field=models.ImageField(default='pic.jpg', upload_to='profile_pic'),
        ),
    ]
