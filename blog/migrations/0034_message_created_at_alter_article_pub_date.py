# Generated by Django 5.0.8 on 2024-09-03 12:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_alter_article_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 9, 3, 12, 25, 6, 675232, tzinfo=datetime.timezone.utc)),
        ),
    ]
