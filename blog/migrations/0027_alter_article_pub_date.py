# Generated by Django 5.0.8 on 2024-08-25 17:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_alter_article_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 8, 25, 17, 1, 47, 34212, tzinfo=datetime.timezone.utc)),
        ),
    ]
