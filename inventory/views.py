from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import InventoryItems
# Create your views here.


def itemsView(req):
    all_inv_items = InventoryItems.objects.all()
    return render(req, 'inventory.html', {'all_items': all_inv_items})


def addItem(req):
    title = req.POST['title']
    author = req.POST['author']
    quantity = req.POST['quantity']
    new_item = InventoryItems(title=title, author=author, quantity=quantity)
    new_item.save()
    return redirect("/inventory/")


def deleteItem(req, inv_id):
    item_del = InventoryItems.objects.get(id=inv_id)
    item_del.delete()
    return redirect("/inventory/")
