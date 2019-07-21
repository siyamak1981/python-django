from django.contrib import admin
from .models import Category
# from .models import Size
from .models import Product,ProductType, ProductTypeAttr, Attributes, AttrValues
from khayyam import JalaliDate as jd
# Register your models here.

from .models import Category, Product
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('title',)}

    def created_at(self, obj):
            return jd(obj.created)
    
    
    def published(self, obj):
        return jd(obj.published_at)

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    
    actions_on_bottom = True
    #  
    # def created_at(self, obj):
    #     return jd(obj.created)
    
    
    # def updated_at(self, obj):
    #     return jd(obj.updated)

@admin.register(ProductTypeAttr)
class ProductTypeAttrAdmin(admin.ModelAdmin):
    pass
    # list_display = ['name']
    # prepopulated_fields = {'slug': ('name',)}
    # search_fields = ('name', 'content')
   
#     actions_on_bottom = True
    
    # def created_at(self, obj):
    #     return jd(obj.created)
    
    
    # def updated_at(self, obj):
    #     return jd(obj.updated)


@admin.register(Attributes)    
class AttributesAdmin(admin.ModelAdmin):
    list_display = ['name']
    # prepopulated_fields = {'slug': ('name',)}


@admin.register(AttrValues)
class AttrValuesAdmin(admin.ModelAdmin):
    list_display = ['name']
    # prepopulated_fields = {'slug': ('name',)}

# @admin.register(Size)
# class SizeAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'category', 'available', 'published', 'created_at']
    list_filter = ['available', 'created', 'updated',]
    list_editable = ['available', 'price']
    prepopulated_fields = {'slug': ('name',)}

    fieldsets = [
        ('main', { 
            'fields': ( 
                    ('name', 'slug'), 
                    ('status', 'category') 
                ),
            }
        ),

        ('Advanced_options', { 
            'fields': (
                    'banner',
                    'banner1',
                    'banner2',
                    'summary',
                    'content',
                    'published_at',
                    'price',
                    'discount',
                    'size',
                    'color',
                    
                ),
            'classes': ('collapse',)
            },

        ),
    ]

    def created_at(self, obj):
        return jd(obj.created)
    
    
    def published(self, obj):
        return jd(obj.published_at)

    # def get_tags(self, obj):
    #     return ", ".join([t.name for t in obj.tag.all()])

    def is_published(self, obj):
        published = 1
        return obj.status == published
    
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return super().has_delete_permission(request)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('published_at',)
        return []
    is_published.boolean = True