# Generated by Django 2.2.6 on 2019-10-24 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mood_sense', '0003_auto_20191024_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='mood',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='mood/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='mood',
            name='characteristic',
            field=models.CharField(choices=[('10', 'No pain'), ('9', 'Very mild'), ('8', 'Discomforting'), ('7', 'Tolerable'), ('6', 'Distressing'), ('5', 'Very distressing'), ('4', 'Intense'), ('3', 'Very intense'), ('2', 'Utterly horrible'), ('1', 'Excruciating unbearable'), ('0', 'Unimaginable unspeakable')], default='1', max_length=50),
        ),
    ]
