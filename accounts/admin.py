from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, CustmerProfile, CraftsmanProfile
from .forms import CustomUserCreationForm, CustomUserChangeForm

admin.site.site_header = "Royal Service Admin"
admin.site.site_title = "Royal Service Admin Area"
admin.site.index_title = "Welcome to the Royal Service Admin Area"

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email','is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('role','is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','role', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    
class CraftsmanProfileUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CraftsmanProfile
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email','is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('role','is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','role', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(CustmerProfile)
admin.site.register(CraftsmanProfile)
