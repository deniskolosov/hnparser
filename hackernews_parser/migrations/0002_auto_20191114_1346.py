# Generated by Django 2.2.7 on 2019-11-14 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackernews_parser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.URLField(unique=True),
        ),
        migrations.AddConstraint(
            model_name='post',
            constraint=models.UniqueConstraint(fields=('title', 'url'), name='unique_title_url_combo'),
        ),
    ]