from django.db import models
from django.utils.safestring import mark_safe

from product.models import Product
from image.models import Images

class Color(models.Model):
    name = models.CharField(max_length=20, verbose_name='اسم رنگ')
    code = models.CharField(
        max_length=10, blank=True, null=True, verbose_name='کد رنگ'
        )
    
    def __str__(self):
        return self.name 
    
    def color_tag(self):
        if self.code is not None:
            return mark_safe(
                '<p style="background-color:{}">رنگ</p>'.format(self.code))
        else:
            return ""
        
    color_tag.short_description = 'رنگ'
    
    class Meta:
        verbose_name = 'رنگ'
        verbose_name_plural = 'رنگ ها'
        

class Size(models.Model):
    name = models.CharField(max_length=20, verbose_name='سایز')
    code = models.CharField(
        max_length=10, null=True, blank=True, verbose_name='کد سایز'
        )
    
    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = 'سایز'
        verbose_name_plural = 'سایز ها'
    

class VariantsManager(models.Model):
    def get_active_variant(self):
        return self.get_queryset().filter(status=True)


class Variants(models.Model):
    STATUS = (
        ('True', 'فعال'),
        ('False', 'غیر فعال'),
    )
    title = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="ویژگی"
        )
    product = models.ForeignKey(Product, on_delete=models.CASCADE,\
        related_name='variation', verbose_name='محصول')
    color = models.ForeignKey(Color, on_delete=models.SET_NULL,\
        null=True, blank=True, verbose_name='تصویر')
    size = models.ForeignKey(Size, on_delete=models.SET_NULL,\
        blank=True,null=True, verbose_name='سایز')
    image_id = models.IntegerField(default=0, verbose_name='تصویر')
    quantity = models.IntegerField(default=1, verbose_name='تعداد')
    price = models.IntegerField(default=0, verbose_name='قیمت')
    status = models.CharField(max_length=50, choices=STATUS,\
        default=True, verbose_name='وضعیت')
    objects = VariantsManager()
    
    def __str__(self):
        return self.title 
    
    def image(self):
        img = Images.objects.get(id=self.image_id)
        if img.id is not None: 
            var_img = img.image.url 
        else:
            var_img = ""
        return var_img
    
    image.short_description = 'تصویر'
    
    def image_tag(self):
        img = Images.objects.get(id=self.image_id)
        if img.id is not None:
            return mark_safe('<img src="{}" height="50"/>'\
                .format(img.image.url))
        else:
            return ""
        
    image_tag.short_description = 'تصویر'
    
    def price_th(self):
        return f"{self.price:,}"
    
    price_th.short_description = 'قیمت'
    
    class Meta:
        verbose_name = 'تنوع'
        verbose_name_plural = 'تنوع ها'    
    