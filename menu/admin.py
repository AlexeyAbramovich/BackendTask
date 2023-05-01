from django import forms
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import MenuItem, Menu


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'


class MenuItemAdmin(MPTTModelAdmin):
    form = MenuItemForm


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Menu)
