# Generated by Django 2.1.7 on 2019-04-08 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ratelyyDatabase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='origin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ratelyyDatabase.Country'),
        ),
    ]
