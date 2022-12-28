from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import *


# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['pk','email','username','first_name','last_name']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields':('email','first_name','last_name','is_teamleader','is_manager','is_employer')}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields':('is_teamleader','is_manager','is_employer')}),
    )


admin.site.register(User,CustomUserAdmin)
admin.site.register(filesend)