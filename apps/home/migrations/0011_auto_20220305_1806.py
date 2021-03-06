# Generated by Django 3.2 on 2022-03-05 12:06

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_questionnaire_answers'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer', models.TextField()),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='team/')),
                ('position', models.CharField(max_length=50)),
                ('facebook', models.CharField(max_length=255)),
                ('twitter', models.CharField(max_length=255)),
                ('linkedin', models.CharField(max_length=255)),
                ('instagram', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Команда',
                'verbose_name_plural': 'Команды',
            },
        ),
        migrations.DeleteModel(
            name='Questionnaire',
        ),
        migrations.AlterModelOptions(
            name='partners',
            options={'verbose_name': 'партнёра', 'verbose_name_plural': 'Партнёры'},
        ),
        migrations.AlterModelOptions(
            name='price',
            options={'verbose_name': 'цена', 'verbose_name_plural': 'Цена'},
        ),
        migrations.RenameField(
            model_name='partners',
            old_name='link_partners',
            new_name='link_partner',
        ),
        migrations.RemoveField(
            model_name='service',
            name='date',
        ),
        migrations.AlterField(
            model_name='partners',
            name='image',
            field=models.ImageField(upload_to='parners/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='price',
            name='description',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price_tarif',
            field=models.CharField(help_text='$45 / Месяц или $Бесплатно / Месяц', max_length=250, null=True, verbose_name='цена'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='service/', verbose_name='Фото'),
        ),
    ]
