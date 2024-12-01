from django.contrib import admin

from .models import Brand

import admin_thumbnails

@admin.register(Brand)
@admin_thumbnails.thumbnail('image', 'تصویر برند')
class BrandAdmin(admin.ModelAdmin):
    list_display = ['title', 'title_eng', 'image_thumbnail']
    prepopulated_fields = {'slug': ('title_eng')}

