# Generated by Django 4.0.1 on 2022-05-09 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dari', '0009_alter_category_image_alter_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='transaction',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
