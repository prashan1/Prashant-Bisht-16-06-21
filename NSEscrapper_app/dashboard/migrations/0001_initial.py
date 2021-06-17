# Generated by Django 3.2 on 2021-06-16 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockMarket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ceOI', models.DecimalField(decimal_places=4, max_digits=7)),
                ('ceCOI', models.DecimalField(decimal_places=4, max_digits=7)),
                ('ceV', models.DecimalField(decimal_places=4, max_digits=7)),
                ('ceIV', models.DecimalField(decimal_places=4, max_digits=7)),
                ('ceLTP', models.DecimalField(decimal_places=4, max_digits=7)),
                ('ceCHNG', models.DecimalField(decimal_places=4, max_digits=7)),
                ('ceBQ', models.DecimalField(decimal_places=4, max_digits=7)),
                ('ceBP', models.DecimalField(decimal_places=4, max_digits=7)),
                ('ceAP', models.DecimalField(decimal_places=4, max_digits=7)),
                ('ceAQ', models.DecimalField(decimal_places=4, max_digits=7)),
                ('strikePrice', models.DecimalField(decimal_places=4, max_digits=7)),
                ('peBQ', models.DecimalField(decimal_places=4, max_digits=7)),
                ('peBP', models.DecimalField(decimal_places=4, max_digits=7)),
                ('peAP', models.DecimalField(decimal_places=4, max_digits=7)),
                ('peAQ', models.DecimalField(decimal_places=4, max_digits=7)),
                ('peCHNG', models.DecimalField(decimal_places=4, max_digits=7)),
                ('peLTP', models.DecimalField(decimal_places=4, max_digits=7)),
                ('peIV', models.DecimalField(decimal_places=4, max_digits=7)),
                ('peV', models.DecimalField(decimal_places=4, max_digits=7)),
                ('peCOI', models.DecimalField(decimal_places=4, max_digits=7)),
                ('peOI', models.DecimalField(decimal_places=4, max_digits=7)),
                ('globalceTOTOI', models.DecimalField(decimal_places=4, max_digits=7)),
                ('globalceTOVOI', models.DecimalField(decimal_places=4, max_digits=7)),
                ('globalpeTOTOI', models.DecimalField(decimal_places=4, max_digits=7)),
                ('globalpeTOVOI', models.DecimalField(decimal_places=4, max_digits=7)),
            ],
            options={
                'ordering': ['strikePrice'],
            },
        ),
    ]
