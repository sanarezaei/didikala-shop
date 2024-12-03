# Generated by Django 5.1.3 on 2024-12-03 16:22

import image.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='عنوان')),
                ('image', models.ImageField(blank=True, upload_to=image.models.upload_image_path, verbose_name='تصویر')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=set, to='product.product')),
            ],
        ),
    ]
