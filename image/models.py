from django.db import models
from django.utils.safestring import mark_safe

from product.models import Product

import os 
import random 

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext 

def upload_image_path(instance, filename):
    new_id = random.randint(1, 999999)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_id}-{instance.title}{ext}"
    return f"gallery/{final_name}"

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=set, blank=True, null=True) 
    title = models.CharField(max_length=50, blank=True, verbose_name='عنوان') 
    image = models.ImageField(blank=True, upload_to=upload_image_path,\
        verbose_name='تصویر')
    
    def __str__(self):
        return self.title 
    
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.ulr))
    
    image_tag.shortcut_description = 'تصویر'
    