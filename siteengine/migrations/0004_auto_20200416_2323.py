# Generated by Django 3.0.5 on 2020-04-16 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteengine', '0003_categories_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallpaperimg',
            name='image',
            field=models.ImageField(height_field='height', upload_to='images/', width_field='width'),
        ),
    ]
