# Generated by Django 2.2.5 on 2022-01-13 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InlineSpeedSkates', '0003_remove_review_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='email',
            field=models.EmailField(default='', max_length=255, verbose_name='email address'),
        ),
    ]
