# Generated by Django 3.1 on 2022-06-08 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='product',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='category_id',
        ),
    ]