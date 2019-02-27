from django.contrib import admin
from .models import Concerns, Companies, Brands, Products
# Register your models here.
class ConcernsAdmin(admin.ModelAdmin):
    list_display = ("name", "rating", "id",)
    search_fields = ["name", "rating", "id",]

class CompaniesAdmin(admin.ModelAdmin):
    list_display = ("name","concern_rating", "logo", "concern", "id",)
    search_fields = ["name","concern_rating", "logo", "concern", "id",]

class BrandsAdmin(admin.ModelAdmin):
    list_display = ("id","name", "logo", "wiki", "company", "concern", "created", "updated",)
    search_fields = ["id","name", "logo", "wiki", "company", "concern", "created", "updated",]
    autocomplete_fields = ("concern", "company",)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ("id","name",  "logo", "wiki", "ean", "image", "group", "brand", "concern", "concern_rating", "created", "updated",)
    search_fields = ["id","name",  "logo", "wiki", "ean", "image", "group", "brand", "concern", "concern_rating", "created", "updated",]
    autocomplete_fields = ("brand", "concern",)

admin.site.register(Concerns, ConcernsAdmin)
admin.site.register(Companies, CompaniesAdmin)
admin.site.register(Brands, BrandsAdmin)
admin.site.register(Products, ProductsAdmin)
