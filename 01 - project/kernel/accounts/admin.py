from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import User, Profile
# Register your models here.



class ProfileInline(admin.TabularInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

    fields = [( 'location', 'pic')]


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


    inlines = (ProfileInline,)
    search_fields = ('email', 'last_name')
    list_filter = ('is_active', 'is_staff')
    list_display = ('email', 'first_name', 'last_name', 'get_location', 'is_active')
    search_fields = ('first_name', 'email', 'profile__location')
    list_select_related = ('profile',)
    ordering = ('email',)




    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)

    def get_location(self, instance):
        return instance.profile.location

    get_location.short_description = 'location'

