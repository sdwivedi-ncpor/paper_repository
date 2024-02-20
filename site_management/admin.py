from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUsers #, Department, Group
from .forms import CustomUserCreationForm


class UserAdmin(BaseUserAdmin):
    model = CustomUsers
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2')}
        ),
    )
    ordering = ('email',)
admin.site.register(CustomUsers, UserAdmin)
# admin.site.register(Department)
# admin.site.register(Group)