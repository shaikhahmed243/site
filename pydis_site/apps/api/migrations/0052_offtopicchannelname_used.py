# Generated by Django 2.2.11 on 2020-03-30 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0051_create_news_setting'),
    ]

    operations = [
        migrations.AddField(
            model_name='offtopicchannelname',
            name='used',
            field=models.BooleanField(default=False, help_text='Whether or not this name has already been used during this rotation'),
        ),
    ]
