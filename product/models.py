# from django.db import models

# from category.models import Category

# import os
# import random

# def get_filename(filepath):
#     base_name = os.path.basename(filepath)
#     name, ext = os.path.splitext(base_name)
#     return name, ext

# def upload_image_path(instance, filename):
#     new_id = random.randint(1, 999999)
#     name, ext = get_filename_ext(filename)
#     final_name = f"{new_id}-{instance.title}{ext}"
#     return f"products/{final_name}" 

# class Product(models.Model):
#     category = models.ForeignKey(
#         Category, on_delete=models.SET_NULL, null=True, verbose_name='دسته'
#         )
#     brand 
#     title 
#     title_eng 
#     keyword 
#     variant 
#     description
#     image 
#     price 
#     amount 
#     all_sale 
#     view_count 
#     details 
#     analyze 
#     status 
#     slug 
#     create_at 
#     objects 
#     favorite 