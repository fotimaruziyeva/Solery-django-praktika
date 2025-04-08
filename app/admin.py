from django.contrib import admin
from .models import Shop,Blog,Faq,Contact,Categories,BlogCategories

admin.site.register((Blog,Categories,BlogCategories))

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('title','price','discount_price','image')
    

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question','answer')

    

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('firstname','lastname','email','subject','message')
    
