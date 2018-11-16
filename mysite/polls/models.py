
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.conf import settings
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() -  datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    
class Product(models.Model):
    pdes = models.CharField(max_length=48) # description 
    price = models.IntegerField(default=0) # price of product
    prep = models.FloatField(default=0.0) # time for preperation
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.pdes + " " + str(self.price) + " " + str(self.id)

class Unit(models.Model): 
    unit_des = models.CharField(max_length=13) # kg, m, box, etc     
    def __str__(self):
        return self.unit_des


class Part(models.Model): # Raw material 
    pdes = models.CharField(max_length=48) # material description
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE) # the forigen key is the id of question   
    stock = models.FloatField(default=0.0) # How Much are in current stock
    lt = models.FloatField(default=1.0) # time to deliver
    sshigh = models.FloatField(default=0) 
    sslow = models.FloatField(default=0) 
    slug = models.SlugField(max_length=48)
    def __str__(self): 
        return self.pdes + " " + str(self.unit) + " " + str(self.stock) + " " + str(self.lt)

class PartsInProduct(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quant = models.FloatField(default=0.0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    class Meta:
        unique_together = (("part", "product"),) # used for double column primary key
    def __str__ (self): ##### probley not ok to be set 
        return self.quant

class Supplier(models.Model):
    name = models.CharField(max_length=200) #supplier name
    adress = models.CharField(max_length=200) #supplier adress
    tel = models.CharField(max_length=200) #supplier telephone
    mail = models.EmailField(max_length=200) # supplier mail
    slug = models.SlugField(max_length=200)
    def __str__(self):
        return self.name + " " + str(adress) + " " + str(tel) + " " + str(mail)

class SupPrice(models.Model):
    supplier = models.ForeignKey(Supplier,null=False, on_delete=models.CASCADE) #supplier name
    part = models.ForeignKey(Part, null=False, on_delete=models.CASCADE)
    price= models.FloatField(max_length=200)
    slug = models.SlugField(max_length=248) 
    class Meta:
        unique_together = (("supplier", "part"),)  # used for double column primary key
    def __str__(self):
        return str(self.supplier) + " " + str(part) + " " + str(price)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #costumer ID
    orderDate = models.DateTimeField(auto_now_add=True) #the date of order creation
    ORDER_STATUS = (
        ('W', 'WAITING'),
        ('R', 'READY'),
        ('T', 'TAKE'),
    )
    orderStatus = models.CharField(max_length=1, choices=ORDER_STATUS, default='WAITING') 
    remarks = models.CharField(max_length=300)  #remarks of the order
    ifSupplied = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user) + " " +str(self.orderDate) +" " + str(self.remarks) + " " +str(self.orderStatus) + " " + str(self.ifSupplied)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, null=False,on_delete=models.CASCADE) #product ID
    order = models.ForeignKey(Order, null=False,on_delete=models.CASCADE) #order ID
    extra1 = models.CharField(max_length=200)#extra1 if have
    extra2 = models.CharField(max_length=200)#extra2 if have
    extra3 = models.CharField(max_length=200)#extra3 if have
    extra4 = models.CharField(max_length=200)#extra4 if have
    extra5 = models.CharField(max_length=200)#extra5 if have
    quant = models.IntegerField()
    ifReady = models.IntegerField(null=False)
    class Meta:
        unique_together = (("product", "order"),)  # used for double column primary key

class POrder(models.Model):
    supplier = models.ForeignKey(Supplier, null=False,on_delete=models.CASCADE) #product ID
    orderStatus = models.ForeignKey(Order, null=False,on_delete=models.CASCADE) #product ID
    porderDate = models.DateField() #date of order
    ifSupplied=models.CharField(max_length=1)#if order cames

class POrderItem(models.Model):
    porder = models.ForeignKey(Supplier, null=False,on_delete=models.CASCADE) #product ID
    part = models.ForeignKey(Part, null=False,on_delete=models.CASCADE) #product ID
    quant = models.FloatField(max_length=200)
    class Meta:
        unique_together = (("part", "porder"),)  # used for double column primary key

from django.contrib.auth.models import User

def get_first_name(self):
    return str(self.username)
User.add_to_class("__str__", get_first_name)
