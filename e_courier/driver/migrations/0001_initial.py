# Generated by Django 2.1.1 on 2019-10-03 06:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='driver_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('car_details', models.TextField()),
                ('phone', models.CharField(max_length=12, unique=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Not Available', 'Available'), ('Onrequest', 'Onrequest')], default='Active', max_length=100)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]