# Generated by Django 3.2 on 2022-03-07 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_about_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='icons/')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'О услуге',
                'verbose_name_plural': 'О услугах',
            },
        ),
    ]
