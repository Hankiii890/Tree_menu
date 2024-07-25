from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=255)
    menu_items = models.ManyToManyField(MenuItem, related_name='menus')

    def __str__(self):
        return self.name