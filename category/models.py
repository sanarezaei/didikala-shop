from django.db import models

from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey

import random

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext 

def upload_image_path(instance, filename):
    new_id = random.randint(1, 999999)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_id}-{instance.title}{ext}"
    return f"category/{final_name}"

class Category(MPTTModel):
    STATUS = (
        ("True", "فعال"),
        ("False", "غیر فعال")
    )
    parent = TreeForeignKey(
        'self', blank=True, null=True, related_name='children', 
        on_delete=models.SET_NULL, verbose_name='دسته مادر')
    title = models.CharField(max_length=50, verbose_name='عنوان')
    en_title = models.CharField(max_length=50, verbose_name='عنوان انگلیسی')
    keyword = models.CharField(max_length=250, verbose_name='کلمه کلیدی')
    description = models.CharField(max_length=300, verbose_name='توضیحات')
    status = models.CharField(
        max_length=50, choices=STATUS, verbose_name='وضعیت'
        )
    image = models.ImageField(
        blank=True, upload_to=upload_image_path, verbose_name='تصویر'
        )
    slug = models.SlugField(
        max_length=200, blank=True, null=False, unique=True, allow_unicode=True, verbose_name='عبارت لینک'
        )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='ایجاد شده در تاریخ'
        )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='آپدیت شده در تاریخ'
        )
    
    def __str__(self):
        return self.title 
    
    def get_absolute_url(self):
        return reverse("product_category_list", kwargs={"slug": self.slug})
    
    def category_active(self):
        return self.objects.filter(status=True)
    
    class Meta:
        verbose_name = 'دسته'
        verbose_name_plural = 'دسته بندی'
    
    class MPTTMeta:
        order_insertion_by = ['title']
    