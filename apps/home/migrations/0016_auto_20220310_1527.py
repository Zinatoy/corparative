# Generated by Django 3.2 on 2022-03-10 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_benefits'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='benefits',
            options={'verbose_name': 'преимущество', 'verbose_name_plural': 'Преимущества'},
        ),
        migrations.AlterModelOptions(
            name='faq',
            options={'verbose_name': 'вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
        migrations.AlterModelOptions(
            name='home',
            options={'verbose_name': 'главную', 'verbose_name_plural': 'Главная'},
        ),
        migrations.AlterModelOptions(
            name='price',
            options={'verbose_name': 'цену', 'verbose_name_plural': 'Цена'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'услугу', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': 'команду', 'verbose_name_plural': 'Команды'},
        ),
    ]
