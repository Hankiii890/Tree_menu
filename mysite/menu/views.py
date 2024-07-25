from django.shortcuts import render
from .templatetags.menu_tag import draw_menu

def menu(request, menu_name):
    menu = draw_menu(request, menu_name)
    return render(request, 'menu.html', {'menu': menu})