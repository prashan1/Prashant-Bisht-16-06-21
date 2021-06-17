# Generated by Django 3.2 on 2021-06-17 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20210617_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockmarket',
            name='CEtotOI',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='CEtotVoi',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='PEtotOI',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='PEtotVoi',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='ceaskPrice',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='ceaskQty',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='cebidQty',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='cebidprice',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='cechange',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='cechangeinOpenInterest',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='ceimpliedVolatility',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='celastPrice',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='ceopenInterest',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='cetotalTradedVolume',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='peaskPrice',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='peaskQty',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='pebidQty',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='pebidprice',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='pechange',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='pechangeinOpenInterest',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='peimpliedVolatility',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='pelastPrice',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='peopenInterest',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='petotalTradedVolume',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='strikePrice',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True),
        ),
    ]
