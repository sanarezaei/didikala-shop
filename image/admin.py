from django.contrib import admin

from .models import Images

@admin.register(Images)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'product', 'image_tag']
