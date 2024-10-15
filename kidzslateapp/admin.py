from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Student)

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ('email', 'username', 'is_staff', 'is_active')
#     list_filter = ('email', 'username', 'is_staff', 'is_active')
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Permissions', {'fields': ('is_staff', 'is_active')}),
#         ('Personal', {'fields': ('username',)}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)

# admin.site.register(Student,CustomUser,CustomUserAdmin)