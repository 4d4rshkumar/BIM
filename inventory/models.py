from django.db import models

# Create your models here.


class InventoryItems(models.Model):
    title = models.TextField()
    author = models.TextField(default='null')
    quantity = models.CharField(max_length=3, default='1')


def __str__(self):
    return (self.title)
