# Generated by Django 2.1.7 on 2019-02-27 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ratelyyDatabase', '0005_auto_20190227_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brands',
            name='brand_concern',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ratelyyDatabase.Concerns', verbose_name='Concern'),
        ),
    ]