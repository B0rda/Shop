from Shop_site.celery import app
from django.core.mail import send_mail
from .models import *
from datetime import datetime, timedelta
@app.task()
def cancel():
    today = datetime.now().date() + timedelta(days=-1)
    z = ''
    for i in Zakaz.objects.filter(status='N').filter(trans_date__lte = today):
        i.status = 'C'
        i.save()
        tovarcart = ZakazCart.objects.filter(zakaz__id=i.id)
        for i in tovarcart:
            if i.cathegory == False:
                product = i.product
                product.v_nal += i.count
                product.save()
            else:
                product = i.hozproduct
                product.v_nal += i.count
                product.save()
    return z