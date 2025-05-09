from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = list_display = ("email", "first_name", "last_name", "is_staff")
    search_fields = ("email", "last_name", "first_name")
    ordering = ("last_name", "first_name")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Informations personnelles", {"fields": ("first_name", "last_name", "date_birth")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "is_active", "user_permissions")})
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "first_name", "last_name", "date_birth", "password1", "password2", "is_staff", "is_active")}
        ),
    )