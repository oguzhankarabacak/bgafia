# Generated by Django 2.0.3 on 2019-07-25 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userdata',
            options={'verbose_name_plural': 'Kullanıcı Verileri'},
        ),
        migrations.AlterField(
            model_name='userdata',
            name='city',
            field=models.CharField(choices=[('Konya', 'Konya'), ('Istanbul', 'Istanbul')], max_length=30, verbose_name='city'),
        ),
    ]
