# Generated by Django 3.2 on 2022-03-05 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20220303_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partners',
            name='link_partners',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Ссылка на партнера'),
        ),
    ]
