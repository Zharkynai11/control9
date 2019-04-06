from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=30,blank=False, null = False,verbose_name="Название")
    description = models.TextField(max_length=500,blank=True, null = True,verbose_name="Описание")

class Product(models.Model):
    title = models.CharField(max_length=30, blank=False, null=False, verbose_name="Название")
    description = models.TextField(max_length=500,blank=True, null = True, verbose_name="Описание")
    begin_date = models.DateField(blank=True, null = True, verbose_name="Дата поступления")
    price = models.DecimalField(decimal_places=2,max_digits=10,blank=False, null = False,verbose_name="Цена")
    category = models.ManyToManyField(Category,blank=True, null = True,verbose_name="Категории")

class PhotoProduct(models.Model):
    product = models.OneToOneField(Product,on_delete=models.PROTECT,blank=False, null = False,verbose_name="Продукт")
    image = models.ImageField(upload_to='static/images',blank=False, null = False,verbose_name="Изображение")

class Order(models.Model):
    products = models.ManyToManyField(Product,blank=False, null = False,verbose_name="Список товаров")
    number = models.CharField(max_length=15,blank=False, null = False,verbose_name="Телефон")
    address = models.CharField(max_length=40,blank=True, null = True, verbose_name="Адрес")
    comment = models.TextField(max_length=500,blank=True, null = True,verbose_name="Комментарий")
    created_date = models.DateTimeField(auto_now=True,verbose_name="Дата создания")

# Create your models here.
