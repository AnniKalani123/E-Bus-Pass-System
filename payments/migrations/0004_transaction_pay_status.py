# Generated by Django 3.2 on 2021-05-28 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_alter_transaction_made_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='pay_status',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]