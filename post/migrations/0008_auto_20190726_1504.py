# Generated by Django 2.0.3 on 2019-07-26 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20190726_1452'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_date']},
        ),
        migrations.AlterModelOptions(
            name='userpost',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterField(
            model_name='userpost',
            name='comment_number',
            field=models.IntegerField(default=0),
        ),
    ]
