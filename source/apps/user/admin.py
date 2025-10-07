from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User

@admin.register(User)
class AdminUser(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ("email", "is_staff", "is_active", "full_name")
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
            (None, {"fields": ("email", "password", "first_name", "last_name")}),
            ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
        )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("first_name", "last_name", "email")
    ordering = ("email",)


    def full_name(self, obj):
        return f"{obj.first_name}  {obj.last_name}"