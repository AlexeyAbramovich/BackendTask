from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Menu(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Menus"


class MenuItem(MPTTModel):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_items')

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']
