# Generated by Django 2.1.7 on 2019-02-26 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ratelyyDatabase', '0004_auto_20190226_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='brands',
            name='brand_concern',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ratelyyDatabase.Concerns'),
        ),
        migrations.AlterField(
            model_name='products',
            name='brands_id_brand',
            field=models.ForeignKey(db_column='brands_id_brand', on_delete=django.db.models.deletion.CASCADE, to='ratelyyDatabase.Brands', verbose_name='Brand'),
        ),
    ]