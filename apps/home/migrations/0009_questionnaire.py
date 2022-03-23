# Generated by Django 3.2 on 2022-03-05 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_partners_link_partners'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.CharField(max_length=100)),
                ('answers', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'вопрос',
                'verbose_name_plural': 'Часто задаваемые вопросы',
            },
        ),
    ]