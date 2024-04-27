from django.contrib import admin
from . import models
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields= {'slug':('name',)}

admin.site.register(models.Category, CategoryAdmin )