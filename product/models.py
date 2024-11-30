# from django.db import models

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

    