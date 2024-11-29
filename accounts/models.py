from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name='نام',
        related_name='profile'
        )
    phone = models.CharField(max_length=20, blank=True, verbose_name='تلفن')
    national_code = models.CharField(
        max_length=20, blank=True, verbose_name='کد ملی', default='_'
        )
    profile_pic = models.ImageField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
        
    def __str__(self):
        return self.user.username
    
    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name
    
    user_name.short_description = 'نام کاربری'
    profile_pic.short_description = 'تصویر'
    

class AddressProfile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='کاربر'
        )
    full_name = models.CharField(
        max_length=60, blank=True, verbose_name='نام و نام خانوادگی'
        )
    phone = models.CharField(max_length=20, blank=True, verbose_name='تلفن')
    province = models.CharField(max_length=20, blank=True, verbose_name='استان')
    city = models.CharField(max_length=20, blank=True, verbose_name='شهر')
    address = models.CharField(
        max_length=150, blank=True, verbose_name='آدرس پستی'
        )
    post_code = models.IntegerField(
        blank=True, null=True, verbose_name='آدرس پستی'
        )
    selected = models.BooleanField(default=False, verbose_name='آدرس منتخب')
    
    def user_name(self):
        self.full_name
        
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'آدرس کاربر'
        verbose_name_plural = 'آدرس کاربران'
        
        
    
    