
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from django.http import HttpResponseRedirect


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
    pdes = models.CharField(max_length=48)  # description
    price = models.IntegerField(default=0)  # price of product
    prep = models.FloatField(default=0.0)  # time for preparation


    def get_absolute_url(self):
        return reverse('polls:product_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.pdes

    def get_name(self):
        return str(self.pdes) + " // " + str(self.price) + " // " + str(self.id)


class Extras(models.Model):
    pdes = models.CharField(max_length=48) # description
    price = models.IntegerField(default=0) # price of product
    productExtra = models.ManyToManyField(Product) #extra to product
    def __str__(self):
        return self.pdes


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

    def __str__(self):
        return self.pdes + " " + str(self.unit) + " " + str(self.stock) + " " + str(self.lt)


class PartsInProduct(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quant = models.FloatField(default=0.0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("part", "product"),) # used for double column primary key

    def __str__ (self): ##### probably not ok to be set
        return self.quant


class Supplier(models.Model):
    name = models.CharField(max_length=200) #supplier name
    address = models.CharField(max_length=200) #supplier adress
    tel = models.CharField(max_length=200) #supplier telephone
    mail = models.EmailField(max_length=200) # supplier mail
    """def __str__(self):
        return self.name + " " + str(address) + " " + str(tel) + " " + str(mail)"""


class SupPrice(models.Model):
    supplier = models.ForeignKey(Supplier,null=False, on_delete=models.CASCADE) #supplier name
    part = models.ForeignKey(Part, null=False, on_delete=models.CASCADE)
    price= models.FloatField(max_length=200)


    class Meta:
        unique_together = (("supplier", "part"),)  # used for double column primary key
    """def __str__(self):
        return str(self.supplier) + " " + str(part) + " " + str(price)"""


class Components(models.Model):
    pdes = models.CharField(max_length=48) # description
    product = models.ForeignKey(Product, on_delete=models.CASCADE) #component to product


    def __str__(self):
        return self.pdes


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #costumer ID
    orderDate = models.DateTimeField(auto_now_add=True) #the date of order creation
    orderPick=models.DateTimeField(auto_now=False)
    ORDER_STATUS = (
        ('W', 'WAITING'),
        ('R', 'READY'),
        ('T', 'TAKE'),
    )
    orderStatus = models.CharField(max_length=1, choices=ORDER_STATUS, default='WAITING') 
    remarks = models.CharField(max_length=300, default=".")  #remarks of the order
    ifSupplied = models.BooleanField(default=False)
    product1 = models.ForeignKey(Product, null=False, on_delete=models.CASCADE, related_name="pro1")  # product ID
    product2 = models.ForeignKey(Product, null=False, on_delete=models.CASCADE, related_name="pro2", default=51)  # product ID
    product3 = models.ForeignKey(Product, null=False, on_delete=models.CASCADE, related_name="pro3", default=51)  # product ID
    extra1 = models.ForeignKey(Extras, on_delete=models.CASCADE, related_name="ex1", default=5)  # extra1 if have
    extra2 = models.ForeignKey(Extras, on_delete=models.CASCADE, related_name="ex2", default=5)  # extra2 if have
    extra3 = models.ForeignKey(Extras, on_delete=models.CASCADE, related_name="ex3", default=5)  # extra3 if have
    extra4 = models.ForeignKey(Extras, on_delete=models.CASCADE, related_name="ex4", default=5)  # extra4 if have
    extra5 = models.ForeignKey(Extras, on_delete=models.CASCADE, related_name="ex5", default=5)  # extra5 if have
    component1 = models.ForeignKey(Components, on_delete=models.CASCADE, related_name="comp1", default=4)  # component1 if have
    component2 = models.ForeignKey(Components, on_delete=models.CASCADE, related_name="comp2", default=4)  # component2 if have
    component3 = models.ForeignKey(Components, on_delete=models.CASCADE, related_name="comp3", default=4)  # component3 if have
    component4 = models.ForeignKey(Components, on_delete=models.CASCADE, related_name="comp4", default=4)  # component4 if have
    component5 = models.ForeignKey(Components, on_delete=models.CASCADE, related_name="comp5", default=4)  # component5 if have

    def get_absolute_url(self):
        return reverse('polls:order_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.user) + " " + str(self.orderDate) + " " + str(self.remarks) + " " + str(self.orderStatus) +\
               " " + str(self.ifSupplied) + " " + str(self.orderPick) + " " + str(self.id)

    def get_name(self):
        return str(self.user) + " //product1: " + str(self.product1) + " ,product2: " + str(self.product2) + " ,product3: " + str(self.product3) + " // " + str(self.orderDate) + " // " + str(self.orderStatus) + " // " + str(self.id)

class OrderItem(models.Model):
    quant = models.IntegerField()
    product = models.ForeignKey(Product, null=False,on_delete=models.CASCADE) #product ID
    order = models.ForeignKey(Order, null=False,on_delete=models.CASCADE) #order ID
    extra1 = models.ForeignKey(Extras, on_delete=models.CASCADE, related_name="ex11")#extra1 if have
    extra2 = models.ForeignKey(Extras, on_delete=models.CASCADE, related_name="ex21")#extra2 if have
    extra3 = models.ForeignKey(Extras, on_delete=models.CASCADE, related_name="ex31")#extra3 if have
    extra4 = models.ForeignKey(Extras, on_delete=models.CASCADE, related_name="ex41")#extra4 if have
    extra5 = models.ForeignKey(Extras, on_delete=models.CASCADE, related_name="ex51")#extra5 if have
    ifReady = models.IntegerField(null=False)

    class Meta:
        unique_together = (("product", "order", ),)  # used for double column primary key


class POrder(models.Model):
    supplier = models.ForeignKey(Supplier, null=False,on_delete=models.CASCADE) #product ID
    orderStatus = models.ForeignKey(Order, null=False,on_delete=models.CASCADE) #status ID
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
