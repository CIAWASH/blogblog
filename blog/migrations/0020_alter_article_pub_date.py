# Generated by Django 5.0.8 on 2024-08-25 16:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_alter_article_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 8, 25, 16, 22, 32, 752710, tzinfo=datetime.timezone.utc)),
        ),
    ]