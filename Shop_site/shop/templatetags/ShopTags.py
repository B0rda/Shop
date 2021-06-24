from django import template
from shop.models import *

register = template.Library()


@ register.simple_tag()
def cathegory_list():
    return Cathegory.objects.all()

@ register.simple_tag()
def hozcathegory_list():
    return HozCathegory.objects.all()


@ register.inclusion_tag('special_produc_tpl.html')
def special_products1(z = 'product'):
    if z == 'product':
        special_products1 = Product.objects.filter(percent__gte = 1).order_by('?')[:4]
    else :
        special_products1 = HozProduct.objects.filter(percent__gte=1).order_by('?')[:4]
    return {'special_products1':special_products1,'z':z}

@register.inclusion_tag('random_cathegory.html')
def random_cathegory(z = 'product', count = 3):
    if z == 'hozproduct':
        cathegorys = HozCathegory.objects.order_by('?')[:count]
    else:
        cathegorys = Cathegory.objects.order_by('?')[:count]
    return {'cathegorys':cathegorys,'type':z}