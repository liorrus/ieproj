
from django.db import models

from django.utils import timezone
import datetime

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
"""
class SupPrice(models.Model):
    supplier = models.ForeignKey(Supplier,null=False, on_delete=models.CASCADE) #supplier name
    part = models.ForeignKey(Parts, null=False, on_delete=models.CASCADE)
    price=models.FloatField(max_length=200)
    class Meta:
        unique_together = (("supplier", "part"),)  # used for double column primary key

class Costumer(models.Model):
    fname = models.CharField(max_length=200, null=False) #costumer first name
    lname= models.CharField(max_length=200, null=False)#costumer last name
    mail = models.EmailField(max_length=200,null=False) # costumer mail
    gender= models.CharField(max_length=1, null=False)

class OrderStatus(models.Model):
    ordstatus=models.IntegerField(max_length=2, null=False) #open, ready, close

class Orders(models.Model):
    costumer = models.ForeignKey(Costumer, null=False, on_delete=models.CASCADE) #costumer ID
    orderDate=models.models.DateTimeField(default=datetime.now, blank=True) #the date of order creation
    orderStatus=models.ForeignKey(OrderStatus,null=False,on_delete=models.CASCADE) #status of order
    remarks=models.CharField(max_length=300)  #remarks of the order
    ifSupplied=models.IntegerField(max_length=1, null=False)

class OrderItems(models.Model):
    product=models.ForeignKey(Product, null=False,on_delete=models.CASCADE) #product ID
    order=models.ForeignKey(Orders, null=False,on_delete=models.CASCADE) #order ID
    extra1=models.CharField(max_length=200)#extra1 if have
    extra2=models.CharField(max_length=200)#extra2 if have
    extra3=models.CharField(max_length=200)#extra3 if have
    extra4=models.CharField(max_length=200)#extra4 if have
    extra5=models.CharField(max_length=200)#extra5 if have
    quant=models.IntegerField(max_length=200)
    orderStatus=models.ForeignKey(Orders,max_length=1)
    class Meta:
        unique_together = (("product", "order"),)  # used for double column primary key

class POrders(models.Model):
    supplier=models.ForeignKey(Supplier, null=False,on_delete=models.CASCADE) #product ID
    orderStatus=models.ForeignKey(Orders, null=False,on_delete=models.CASCADE) #product ID
    porderDate=models.DateField() #date of order
    ifSupplied=models.CharField(max_length=1)#if order cames

class POrderItems(models.Model):
    porder=models.ForeignKey(Supplier, null=False,on_delete=models.CASCADE) #product ID
    part=models.ForeignKey(Parts, null=False,on_delete=models.CASCADE) #product ID
    quant=models.FloatField(max_length=200)
"""


