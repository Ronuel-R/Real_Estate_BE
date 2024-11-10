from django.contrib import admin
from .models.property_model import Property
from .models.custom_user_model import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password','api_secret_key')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    # readonly_fields = ('api_secret_key',)

admin.site.register(Property)
admin.site.register(CustomUser,CustomUserAdmin)
