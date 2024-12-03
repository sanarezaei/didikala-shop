from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin

from .models import Category
from product.models import Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'status']
    list_filter = ['status']
    prepopulated_fields = {'slug': ('en_title', )}


class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = 'title'
    list_display = (
        'tree_actions', 'indented_title', 'related_products_count', 'related_products_cumulative_count'
        )
    list_display_links = ('indented_title ')
    
    def get_queryset(self, request): 
        qs = super().get_queryset(request)
        
        # Add cumulative products count
        qs = Category.objects.add_related_count(
            qs, 
            Product,
            'category',
            'products_cumulative_count', 
            cumulative=True   
        )
        
        # Add non cumulative products count
        qs = Category.objects.add_related_count(
            qs,
            product, 
            'category', 
            'products_count',
            cumulative=False
        )
        return qs 
    
    def related_products_count(self, instance):
        return instance.products_count 
    
    related_products_count.short_description = 'محصولات مرتبط (با این دسته )'
    
    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    
    related_products_cumulative_count.short_description = \
        'محصولات مرتبط (با این شاخه)'
        