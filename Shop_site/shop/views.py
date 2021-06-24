from django.shortcuts import render, redirect
from shop.models import *
from django.db.models import F
from django.views.generic import ListView,DetailView,CreateView
from django.db.utils import IntegrityError
from django.db.models import Count
from .forms import *
from django.contrib.auth import login, logout
from datetime import datetime, date, time, timedelta

def register(request):
    if request.method == 'POST':
        form = NewUser(data = request.POST)
        if form.is_valid():
            try:
                form.save()
            except IntegrityError:
                form.errors['email'] = "Пользователь с такой почтой уже зарегестрирован"
                return render(request, 'register.html', {'form': form})
            return redirect("/")
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = NewUser()
        return render(request,'register.html',{'form':form})


def loginuser(request):
    if request.method == 'POST':
        form = AuthUser(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect("/")
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthUser()
        return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect("/")

def index(request):
    bestproduct = Product.objects.order_by('-percent')[:4]
    besthoz = HozProduct.objects.order_by('-percent')[:4]
    return render(request,'index.html',{"bestproduct":bestproduct,"besthoz":besthoz})


class Discount_list(ListView):
    template_name = 'kitchen.html'
    context_object_name = 'product_list'
    paginate_by = 2
    def get_queryset(self):
        print(self.request.path_info)
        if self.request.path_info == '/product_discont/':
            return Product.objects.filter(percent__gte=1)
        else :
            return HozProduct.objects.filter(percent__gte=1)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Discount_list, self).get_context_data()
        if self.request.path_info == '/product_discont/':
            context['title'] = 'Продукты со скидкой'
            context['type'] = 'Product'
        else:
            context['title'] = 'Хозяйственные товары со скидкой'
            context['type'] = 'HozProduct'
        return context

class Product_list(ListView):
     template_name = 'kitchen.html'
     context_object_name = 'product_list'
     paginate_by = 2
     def get_queryset(self):
         return Product.objects.filter(cathegory__slug=self.kwargs['slug'])
     def get_context_data(self, *, object_list=None, **kwargs):
         context = super(Product_list, self).get_context_data()
         context['title'] = Cathegory.objects.get(slug = self.kwargs['slug'])
         context['type'] = 'Product'
         context['random_cathegory'] = Cathegory.objects.order_by('?')[:3]
         return context
# Create your views here.

class Single(DetailView):
    template_name = 'single.html'
    context_object_name = 'single'
    model = Product


class HozProduct_list(ListView):
    template_name = 'kitchen.html'
    context_object_name = 'product_list'
    paginate_by = 2

    def get_queryset(self):
        return HozProduct.objects.filter(cathegory__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HozProduct_list, self).get_context_data()
        context['title'] = HozCathegory.objects.get(slug=self.kwargs['slug'])
        context['type'] = 'HozProduct'
        context['random_cathegory'] = HozCathegory.objects.order_by('?')[:3]
        return context

class HozProduct_Single(DetailView):
    template_name = 'single.html'
    context_object_name = 'single'
    model = HozProduct
    def get_context_data(self, **kwargs):
        context = super(HozProduct_Single, self).get_context_data()
        context['type'] = 'HozProduct'
        return context

def cart(request):
    today = datetime.now().date()
    tommorow = datetime.now().date() + timedelta(days=1)
    posle_tommorow = datetime.now().date() + timedelta(days=2)
    messeges = []
    if request.method == 'POST':
        zakaz_date = today
        if request.POST.get('date') == "2":
            zakaz_date = tommorow
        elif request.POST.get('date') == "3":
            zakaz_date = posle_tommorow
        for i in range (len(request.POST.getlist('koko'))):
            if request.POST.getlist('Type')[i] == 'False':
                tovar = Product.objects.get(slug = request.POST.getlist('koko')[i])
                if int(tovar.v_nal) - int(request.POST.getlist('quantity')[i]) < 0:
                    messeges += [str(tovar.name) + '. Осталось в наличии: ' + str(tovar.v_nal)]
            else:
                tovar = HozProduct.objects.get(slug=request.POST.getlist('koko')[i])
                if int(tovar.v_nal) - int(request.POST.getlist('quantity')[i]) < 0:
                    messeges += [str(tovar.name) + '. Осталось в наличии: ' + str(tovar.v_nal)]
        if messeges != []:
            return render(request, 'cart.html',{'today':today,"tommortow":tommorow,"posle_tommorow":posle_tommorow,'messeges':messeges})
        username = User.objects.get(username = (request.user))
        new_zakaz = Zakaz(user = username,final_price = request.POST.get('final_price'),date_create = None,trans_date=zakaz_date)
        new_zakaz.save()
        for i in range (len(request.POST.getlist('koko'))):
            if request.POST.getlist('Type')[i] == 'False':
                tovar = ZakazCart(cathegory = False,product = Product.objects.get(slug = request.POST.getlist('koko')[i]),count = request.POST.getlist('quantity')[i],zakaz = new_zakaz)
                tovar.save()
                Product.objects.filter(slug=request.POST.getlist('koko')[i]).update(v_nal = F('v_nal') - request.POST.getlist('quantity')[i])
            else:
                tovar = ZakazCart(cathegory = True,hozproduct = HozProduct.objects.get(slug = request.POST.getlist('koko')[i]),count = request.POST.getlist('quantity')[i],zakaz = new_zakaz)
                tovar.save()
                HozProduct.objects.filter(slug=request.POST.getlist('koko')[i]).update(v_nal=F('v_nal') - request.POST.getlist('quantity')[i])

        return render(request, 'order_okey.html',{'new_zakaz':new_zakaz})

    return render(request,'cart.html',{'today':today,"tommortow":tommorow,"posle_tommorow":posle_tommorow})

class Orders(ListView):
    template_name = 'orders.html'
    context_object_name = 'orders'
    def get_queryset(self):
        return(Zakaz.objects.filter(user = self.request.user))
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Orders, self).get_context_data()
        context['orders_product'] = ZakazCart.objects.filter(zakaz__user = self.request.user)
        return context

class Search(ListView):
    template_name = 'search.html'
    context_object_name = 'product_list'
    def get_queryset(self):
        print(self.request.GET.get('Search'))
        return(Product.objects.filter(name__icontains = self.request.GET.get('Search')))
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Search, self).get_context_data()
        context['hozproduct_list'] = HozProduct.objects.filter(name__icontains = self.request.GET.get('Search'))
        context['title'] = 'Поиск'
        return context