# Generated by Django 3.2 on 2021-05-28 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20210527_1517'),
        ('payments', '0005_alter_transaction_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='made_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='myapp.user'),
        ),
    ]
