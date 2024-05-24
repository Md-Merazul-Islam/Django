from django.contrib import admin
from .models import Category,Book


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug']
admin.site.register(Category , CategoryAdmin)



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'quantity')
    search_fields = ('title', 'description')
    list_filter = ('categories',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'image')
        }),
        ('Price and Quantity', {
            'fields': ('price', 'quantity')
        }),
        ('Categories', {
            'fields': ('categories',)
        }),
    )
    filter_horizontal = ('categories',)
