# Generated by Django 4.0.1 on 2022-04-21 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dari', '0004_rename_date_cart_day_rename_date_comment_day_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_acitve',
            field=models.BooleanField(default=False),
        ),
    ]
