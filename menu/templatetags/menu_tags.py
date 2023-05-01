from django import template
from django.urls import reverse, resolve
from ..models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    menu_items = MenuItem.objects.filter(parent=None).filter(menu__name__exact=menu_name).order_by('name')
    active_item = None
    current_url = resolve(context['request'].path_info).url_name

    for item in menu_items:
        item.active = False
        if item.url == current_url or (item.url == "" and item.children.filter(url=current_url).exists()):
            item.active = True
            active_item = item

    if active_item:
        active_item = active_item.parent

        while active_item:
            active_item.active = True
            active_item = active_item.parent

    context.update({
        'menu_items': menu_items,
    })

    return ''
