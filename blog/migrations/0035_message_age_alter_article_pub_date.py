# Generated by Django 5.0.8 on 2024-09-04 15:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_message_created_at_alter_article_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 9, 4, 15, 2, 33, 233104, tzinfo=datetime.timezone.utc)),
        ),
    ]
