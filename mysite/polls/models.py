
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
    sshigh = models.FloatField(default=0) # How Much are in current stock
    sslow = models.FloatField(default=0) 
    def __str__(self): 
        return self.pdes

class PartsInProduct(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quant = models.FloatField(default=0.0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    class Meta:
        unique_together = (("part", "product"),) # used for double column primary key
    def __str__ (self): ##### probley not ok to be set 
        return self.quant





class Supplier(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Producttemo(models.Model): 
    desc = models.CharField(max_length=200)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    unit = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    date = models.DateTimeField('date published') 

class Order(models.Model):
    name = models.CharField(max_length=200)
