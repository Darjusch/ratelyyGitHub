# Generated by Django 2.1.7 on 2019-04-16 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratelyyDatabase', '0011_auto_20190416_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stat_counter',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
