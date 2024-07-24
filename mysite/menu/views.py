from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from templatetags.menu_tag import draw_menu


def menu(request, menu_name):
    return render(request, 'menu.html', {'menu': draw_menu(menu_name)})