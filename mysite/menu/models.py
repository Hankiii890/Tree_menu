from django.db import models

from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)


class Menu(models.Model):
    name = models.CharField(max_length=255)
    menu_items = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='menu')
