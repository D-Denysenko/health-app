# Generated by Django 2.2.6 on 2019-10-24 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mood_sense', '0005_auto_20191024_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mood',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='mood',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True),
        ),
    ]
