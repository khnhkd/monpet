# Generated by Django 3.1 on 2022-06-04 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20220604_1813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='describe',
            new_name='description',
        ),
    ]
