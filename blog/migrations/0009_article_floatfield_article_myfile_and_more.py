# Generated by Django 5.0.8 on 2024-08-21 16:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_article_is_published_alter_article_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='floatfield',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='article',
            name='myfile',
            field=models.BinaryField(null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 8, 21, 16, 32, 37, 376971, tzinfo=datetime.timezone.utc)),
        ),
    ]
