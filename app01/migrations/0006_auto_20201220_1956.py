# Generated by Django 3.1.4 on 2020-12-20 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20201220_1955'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='authorofpaper',
            index=models.Index(fields=['author_id'], name='author_id'),
        ),
    ]
