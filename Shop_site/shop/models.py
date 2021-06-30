from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Cathegory(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    photo = models.ImageField(upload_to='cathegory', blank=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Product_list',kwargs={'slug':self.slug})


class HozCathegory(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique=True)
    photo = models.ImageField(upload_to='cathegory', blank=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('HozProduct_list',kwargs={'slug':self.slug})

class Country(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)

    def __str__(self):
        return self.name

class ProductBase(models.Model):
    class Meta:
        abstract = True
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    country = models.ForeignKey(Country, blank=True, on_delete=models.PROTECT)
    photo = models.ImageField(upload_to='product/%Y/%m/%d')
    price = models.DecimalField(max_digits=10, decimal_places=0,validators=[MinValueValidator(0)])
    percent = models.DecimalField(max_digits=2, decimal_places=0,default=0,validators=[MinValueValidator(0)])
    final_price = models.DecimalField(max_digits=10, decimal_places=0,default=0)
    consist = models.TextField(max_length=700, blank=True)
    v_nal = models.DecimalField(max_digits=4,decimal_places=0,default=0,validators=[MinValueValidator(0)])


class Product(ProductBase):
    cathegory = models.ForeignKey(Cathegory, on_delete=models.CASCADE)
    weight_size = models.CharField(max_length=20)
    proteins = models.DecimalField(max_digits=4,decimal_places=1)
    fats = models.DecimalField(max_digits=4,decimal_places=1)
    uglevody = models.DecimalField(max_digits=4,decimal_places=1)
    calories = models.DecimalField(max_digits=4,decimal_places=1)
    Type = models.BooleanField(default=0,editable = False)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("Single",kwargs={'slug':self.slug})


class HozProduct(ProductBase):
    cathegory = models.ForeignKey(HozCathegory,on_delete=models.CASCADE)
    weight = models.CharField(max_length=20)
    Type = models.BooleanField(default=1,editable = False)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('HozProduct_Single',kwargs={'slug':self.slug})



class Zakaz(models.Model):
    STATUS = (
        ('Y', 'Yes'),
        ('N', 'No'),
        ('C', 'Cancel')
    )


    user = models.ForeignKey(User,on_delete=models.CASCADE)
    final_price = models.DecimalField(max_digits=10, decimal_places=0,default=0)
    date_create = models.DateField(auto_now_add=True)
    trans_date = models.DateField(default=now)
    status = models.CharField(max_length=1, choices=STATUS,default='N',verbose_name='Товар передан')
    def __str__(self):
        return str(self.id)


class ZakazCart(models.Model):
    cathegory = models.BooleanField()
    product = models.ForeignKey(Product,on_delete=models.PROTECT,blank=True,null=True)
    hozproduct = models.ForeignKey(HozProduct,on_delete=models.PROTECT,blank=True,null=True)
    count = models.DecimalField(max_digits=4,decimal_places=0,default=0)
    zakaz = models.ForeignKey(Zakaz,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.zakaz)
