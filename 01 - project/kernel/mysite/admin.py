from django.contrib import admin

from .models import Contact


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('title','sku', 'email')
    search_fields = ('fullname','sku', 'email')
    view_on_site = False
    readonly_fields = ('title', 'email', 'message')
    list_filter = ('created_at',)
    list_per_page = 7

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

  