# Generated by Django 5.0.8 on 2024-08-25 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_article_pub_date_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 8, 25, 15, 19, 35, 774751, tzinfo=datetime.timezone.utc)),
        ),
    ]