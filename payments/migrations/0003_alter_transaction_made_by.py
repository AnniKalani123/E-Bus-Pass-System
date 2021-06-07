# Generated by Django 3.2 on 2021-05-27 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20210527_1517'),
        ('payments', '0002_alter_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='made_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='myapp.user'),
        ),
    ]
