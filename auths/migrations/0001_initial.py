# Generated by Django 2.0.3 on 2019-07-22 16:34

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
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=50, verbose_name='ip')),
                ('city', models.CharField(max_length=30, verbose_name='city')),
                ('country', models.CharField(max_length=30, verbose_name='country')),
                ('birthday', models.DateField(null=True, verbose_name='Doğum Tarihi')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Kullanıcı Profili',
            },
        ),
    ]