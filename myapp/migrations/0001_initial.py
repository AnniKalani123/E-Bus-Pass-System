# Generated by Django 3.2 on 2021-04-20 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocationDestination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_id', models.CharField(max_length=20)),
                ('location_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LocationSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_id', models.CharField(max_length=20)),
                ('location_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('address', models.TextField()),
                ('password', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=6)),
                ('age', models.IntegerField()),
                ('Profile_pic', models.FileField(default='pic.jpg', upload_to='profile_pic')),
                ('is_handicaped', models.BooleanField(default=False)),
                ('pass_valid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PassId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_u_id', models.CharField(max_length=30)),
                ('issue_date', models.DateField(auto_now_add=True)),
                ('expiry_date', models.CharField(max_length=30)),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_amount', models.CharField(max_length=10)),
                ('pass_issue_date', models.DateField(auto_now_add=True)),
                ('pass_duration', models.CharField(max_length=30)),
                ('qr_image', models.FileField(default=None, upload_to='AllPass')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.locationdestination')),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.passid')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.locationsource')),
            ],
        ),
    ]
