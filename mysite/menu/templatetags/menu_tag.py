from django import template
from mysite.menu.models import *

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu = Menu.objects.get(name=menu_name)
    menu_items = menu.menu_items.all()
    active_menu_item = None
    for item in menu_items:
        if item.url and register.path.startswith(item.url):
            active_menu_item = item
            break
    return render_menu(menu_items, active_menu_item)


def render_menu(menu_items, active_menu_item):
    result = []
    for item in menu_items:
        if item.parrent:
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