from django.contrib import admin
from shop.models import *


class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


class CathegoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","v_nal")
    prepopulated_fields = {"slug": ('name',)}


class HozCathegoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


class HozProductAdmin(admin.ModelAdmin):
    list_display = ("name", "v_nal")
    prepopulated_fields = {"slug": ('name',)}


def cancel(modeladmin, request, queryset):
    for i in queryset:
        if i.status == 'N':
            i.status = 'C'
            i.save()
            tovarcart = ZakazCart.objects.filter(zakaz__id = i.id)
            for i in tovarcart:
                if i.cathegory == False:
                    product = i.product
                    product.v_nal += i.count
                    product.save()
                else:
                    product = i.hozproduct
                    product.v_nal += i.count
                    product.save()

class ZakazAdmin(admin.ModelAdmin):
    list_display=("id","user","final_price","status","trans_date")
    actions = [cancel]

class ZakazCartAdmin(admin.ModelAdmin):
    list_display = ("zakaz","product","hozproduct","count")
admin.site.register(Cathegory,CathegoryAdmin)
admin.site.register(Country,CountryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(HozProduct,HozProductAdmin)
admin.site.register(HozCathegory,HozCathegoryAdmin)
admin.site.register(Zakaz,ZakazAdmin)
admin.site.register(ZakazCart,ZakazCartAdmin)
# Register your models here.
