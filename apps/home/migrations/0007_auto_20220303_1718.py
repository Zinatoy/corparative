# Generated by Django 3.2 on 2022-03-03 11:18

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20220301_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('link_partners', models.CharField(blank=True, max_length=250, null=True, verbose_name='Название')),
                ('image', models.ImageField(upload_to='partners/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'партнера',
                'verbose_name_plural': 'Партнеры',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_tarif', models.CharField(max_length=100, verbose_name='Название')),
                ('price_tarif', models.CharField(help_text='$45 / Месяц или $Бесплатно / Месяц', max_length=250, null=True, verbose_name='Название')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'цена',
                'verbose_name_plural': 'Цены',
            },
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='services/', verbose_name='Фото'),
        ),
    ]