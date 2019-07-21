from django.contrib import admin
from khayyam import JalaliDate as jd

from . import models
from painless.models.actions import PostableMixin
from painless.models.actions import ExportMixin


# Register your models here.
class CommentInline(admin.StackedInline):
    model = models.Comment
    # max_num = 2
    fields = [
        ('email', 'title',),
        ('parent', 'active'),
        'content'
    ]



@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin, PostableMixin, ExportMixin):
    list_display = ['title', 'slug', 'is_published', 'published', 'category', 'get_tags']
    prepopulated_fields = { "slug": ('title',)}
    list_editable = ['category']
    list_filter = ['status', 'published_at', 'category__title']
    filter_horizontal = ['tag']
    inlines = [CommentInline]
    actions = ['make_published', 'make_draft', 'export_as_json', 'export_as_csv']
    # fields = (
    #     ('title', 'slug',),
    #     ('status', 'category', 'author',),
    #     'tag',
    #     ('published_at', 'banner'),
    #     'summary',
    #     'content',
    # )

    fieldsets = [
        ('main', { 
            'fields': ( 
                    ('title', 'slug'), 
                    ('author', 'status', 'category') 
                ),
            }
        ),

        ('Advanced_options', { 
            'fields': (
                    'tag',
                    'banner',
                    'summary',
                    'content',
                    'published_at',
                ),
            'classes': ('collapse',)
            },

        ),
    ]

    def published(self, obj):
        return jd(obj.published_at)

    def get_tags(self, obj):
        return ", ".join([t.title for t in obj.tag.all()])

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

@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_at', 'updated_at']
    # list_display_links = ['created_at']
    # list_editable = ['title', 'slug']
    list_filter = ['created',]
    prepopulated_fields = { "slug": ('title',)}
    search_fields = ['title']
    # list_per_page = 100
    actions_on_bottom = True
    date_hierarchy = 'created'
    empty_value_display = '--empty--'

    def created_at(self, obj):
        return jd(obj.created)
    
    def updated_at(self, obj):
        return jd(obj.updated)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created', 'updated']

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


# ##########
# ticketing
# ###########3333

# Register your models here.


@admin.register(models.Ticketing)
class TicketingAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    pass
@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass
@admin.register(models.Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    pass


admin.site.site_header = "Sepehr Adminstration"
admin.site.site_title = "Sepehr site admin"
admin.site.index_title = "Welcome to Sepehr dashboard"
