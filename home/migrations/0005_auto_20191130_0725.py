# Generated by Django 2.2.7 on 2019-11-30 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_mostvisitedplaces_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mostvisitedplaces',
            name='ratings',
            field=models.IntegerField(),
        ),
    ]