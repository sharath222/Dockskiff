from django.contrib import admin

from .models import Product, userProducts, UserProfile
# creating a list for the admin page view
@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    list_display = ("user", "first_name", 'last_name', 'phone_number')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   list_display = ("product_name", "product_type", 'product_price')

@admin.register(userProducts)
class userProductsAdmin(admin.ModelAdmin):
    pass