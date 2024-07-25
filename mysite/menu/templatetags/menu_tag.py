from django import template
from ..models import MenuItem, Menu
from django.urls import reverse

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    menu = Menu.objects.get(name=menu_name)
    menu_items = menu.menu_items.all()
    active_menu_item = None
    current_path = context.request.path
    for item in menu_items:
        if item.url and current_path.startswith(item.url):
            active_menu_item = item
            break
    return render_menu(menu_items, active_menu_item)


def render_menu(menu_items, active_menu_item):
    result = []
    for item in menu_items:
        if item.parent:
            continue
        result.append({
            'name': item.name,
            'url': item.url,
            'children': render_children(item.children.all(), active_menu_item)
        })
    return result


def render_children(menu_items, active_menu_item):
    result = []
    for item in menu_items:
        if item == active_menu_item:
            result.append({
                'name': item.name,
                'url': item.url,
                'children': render_children(item.children.all(), active_menu_item)
            })
        else:
            result.append({
                'name': item.name,
                'url': item.url
            })
    return result