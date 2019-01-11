
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from django.http import HttpResponseRedirect
import datetime
from django.urls import path
from django.shortcuts import render, redirect


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
    slug = models.SlugField(default="STRING")

    def get_absolute_url(self):
        return reverse('polls:product_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.pdes

    def get_name(self):
        return str(self.pdes) + " // " + str(self.price)  + "$ // " + str(self.prep)

    def get_prep_time(self):
        return self.prep
    
    #class Meta:
    #    ordering = ('pdes',)


class Unit(models.Model): 
    unit_des = models.CharField(max_length=13) # kg, m, box, etc     

    def __str__(self):
        return self.unit_des


class Part(models.Model): # Raw material 
    pdes = models.CharField(max_length=48) # material description
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE) # the foreign key is the id of question
    stock = models.FloatField(default=0.0) # How Much are in current stock
    lt = models.FloatField(default=1.0) # time to deliver
    sshigh = models.FloatField(default=0) 
    sslow = models.FloatField(default=0)
    slug = models.SlugField(default="STRING")

    def get_absolute_url(self):
        return reverse('polls:part_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.pdes

    def get_name(self):
        return str(self.pdes) + " // " + str(self.stock)
    class Meta:
        ordering = ('pdes',)


class Pip(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quant = models.FloatField(default=0.0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("part", "product"),)  # used for double column primary key

    def get_absolute_url(self):
        return reverse('polls:pip_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.part) + " " + str(self.quant) + " " + str(self.product)

    def get_name(self):
        return str(self.part) + " // " + str(self.quant) + " // " + str(self.product)


class NewExtra(models.Model):
    extra_part = models.ForeignKey(Part, on_delete=models.CASCADE)
    extra_price = models.FloatField(default=0.0)
    extra_product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('polls:newextra_detail', kwargs={'pk': self.pk})

    def __str__(self):
       return str(self.extra_part.pdes) + " " + str(self.extra_product) + " " + str(self.extra_price)  + "$"

    def get_name(self):
        #eturn str(self.extra_part) + " // " + str(self.extra_price) + " // " + str(self.extra_product)
        return str(self.extra_part.pdes) + " " + str(self.extra_product) + " " + str(self.extra_price)  + "$"
    class Meta:
        ordering = ('extra_product','extra_part')


class Supplier(models.Model):
    name = models.CharField(max_length=200)  # supplier name
    address = models.CharField(max_length=200)  # supplier address
    tel = models.CharField(max_length=200)  # supplier telephone
    mail = models.EmailField(max_length=200)  # supplier mail
    slug = models.SlugField(default="STRING")

    def get_absolute_url(self):
        return reverse('polls:supplier_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.name) + " " + str(self.address) + " " + str(self.tel) + " " + str(self.mail)

    def get_name(self):
        return str(self.name) + " // " + str(self.address)


class SupPrice(models.Model):
    supplier = models.ForeignKey(Supplier,null=False, on_delete=models.CASCADE) #supplier name
    part = models.ForeignKey(Part, null=False, on_delete=models.CASCADE)
    price = models.FloatField(max_length=200)
    slug = models.SlugField(default="STRING")

    class Meta:
        unique_together = (("supplier", "part"),)  # used for double column primary key

    def __str__(self):
        return str(self.supplier.name) + " " + str(self.part) + " " + str(self.price)

    def get_absolute_url(self):
        return reverse('polls:supprice_detail', kwargs={'pk': self.pk})

    def get_name(self):
        return str(self.supplier.name) + " // " + str(self.part.pdes) + " // " + str(self.price)
    

class Components(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quant = models.FloatField(default=0.0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # component to product

    def get_absolute_url(self):
        return reverse('polls:components_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.part) + " "  + str(self.product)

    def get_name(self):
        return str(self.part) +  " // " + str(self.product)
    class Meta:
        ordering = ('product','part')


now = datetime.datetime.now()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # costumer ID
    orderDate = models.DateTimeField(auto_now_add=True)  # the date of order creation
    orderPick=models.DateTimeField(blank=True, default=now)
    ORDER_STATUS = (
        ('W', 'WAITING'),
        ('R', 'READY'),
        ('T', 'TAKE'),
    )
    orderStatus = models.CharField(max_length=1, choices=ORDER_STATUS, default='WAITING') 
    remarks = models.CharField(max_length=300, default="-none-")  # remarks of the order
    ifSupplied = models.BooleanField(default=False)
    product1 = models.ForeignKey(Product, null=False, on_delete=models.CASCADE, related_name="pro1")  # product ID
    product2 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="pro2", default=None, null=True, blank=True)  # product ID
    product3 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="pro3", default=None, null=True, blank=True)  # product ID
    extra1 = models.ForeignKey(NewExtra, on_delete=models.CASCADE, related_name="ex1", default=None, null=True, blank=True)  # extra1 if have
    extra2 = models.ForeignKey(NewExtra, on_delete=models.CASCADE, related_name="ex2", default=None, null=True, blank=True)  # extra2 if have
    extra3 = models.ForeignKey(NewExtra, on_delete=models.CASCADE, related_name="ex3", default=None, null=True, blank=True)  # extra3 if have
    extra4 = models.ForeignKey(NewExtra, on_delete=models.CASCADE, related_name="ex4", default=None, null=True, blank=True)  # extra4 if have
    extra5 = models.ForeignKey(NewExtra, on_delete=models.CASCADE, related_name="ex5", default=None, null=True, blank=True)  # extra5 if have
    component1 = models.ForeignKey(Components, on_delete=models.CASCADE, related_name="comp1", null=True, blank=True,)  # component1 if have
    component2 = models.ForeignKey(Components, on_delete=models.CASCADE, related_name="comp2", default=None, null=True, blank=True)  # component2 if have
    component3 = models.ForeignKey(Components, on_delete=models.CASCADE, related_name="comp3", default=None, null=True, blank=True)  # component3 if have
    component4 = models.ForeignKey(Components, on_delete=models.CASCADE, related_name="comp4", default=None, null=True, blank=True)  # component4 if have
    component5 = models.ForeignKey(Components, on_delete=models.CASCADE, related_name="comp5", default=None, null=True, blank=True)  # component5 if have

    def get_absolute_url(self):
        return reverse('polls:order_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.user) + " " + str(self.orderDate) + " " + str(self.remarks) + " " + str(self.orderStatus) +\
               " " + str(self.ifSupplied) + " " + str(self.orderPick)

    def get_name(self):
        return str(self.user) + ": " + str(self.product1) + "- pick: " + str(
            self.orderPick.strftime("%d/%m %H:%M")) + " // " + str(self.orderStatus)+": "

    def get_details(self):
        details = []
        if self.product1.pk!=7 and self.product1.pk!=5:
            return str(details)
        if self.component1 is not None:
            if self.component1.part!=(37 or 36):
                details.append(str(self.component1.part))
        if self.component2 is not None:
            if self.component2.part != (37 or 36):
                details.append(str(self.component2.part))
        if self.component3 is not None:
            if self.component3.part!=(37 or 36):
                details.append(str(self.component3.part))
        if self.component4 is not None:
            if self.component4.part!=(37 or 36):
                details.append(str(self.component4.part))
        if self.component5 is not None:
            if self.component5.part!=(37 or 36):
                details.append(str(self.component5.part))

        if self.extra1 is not None:
            if self.extra1.extra_part!=(27 or 22):
                details.append(str(self.extra1.extra_part))
        if self.extra2 is not None:
            if self.extra2.extra_part!=(27 or 22):
                details.append(str(self.extra2.extra_part))
        if self.extra3 is not None:
            if self.extra3.extra_part != (27 or 22):
                details.append(str(self.extra3.extra_part))
        if self.extra4 is not None:
            if self.extra4.extra_part!=(27 or 22):
                details.append(str(self.extra4.extra_part))
        if self.extra5 is not None:
            if self.extra5.extra_part!=(27 or 22):
                details.append(str(self.extra5.extra_part))

        return str(details)

class POrder(models.Model):
    supplier = models.ForeignKey(Supplier, null=False, on_delete=models.CASCADE)  # product ID
    ORDER_STATUS = (
        ('W', 'WAITING'),
        ('R', 'READY'),
        ('T', 'TAKE'),
    )
    orderStatus = models.CharField(max_length=1, choices=ORDER_STATUS, default='WAITING')
    porderDate = models.DateTimeField(auto_now_add=True)  # the date of order creation
    ifSupplied = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('polls:pord_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.supplier.name) + " " + str(self.orderStatus) + " " + str(self.porderDate)

    def get_name(self):
        return str(self.supplier.name) + " // " + str(self.orderStatus) + " // " + str(self.porderDate) \
               + " // " + str(self.ifSupplied)


class POrderItem(models.Model):
    porder = models.ForeignKey(POrder, null=False,on_delete=models.CASCADE)  # product ID
    supprice = models.ForeignKey(SupPrice, null=False,on_delete=models.CASCADE)  # product ID
    quant = models.FloatField(max_length=200)
    part = models.ForeignKey(Part, null=True,on_delete=models.CASCADE, default=1)  # product ID

    class Meta:
        unique_together = (("supprice", "porder"),)  # used for double column primary key

    def get_absolute_url(self):
        return reverse('polls:porderitem_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.porder) + " " + str(self.supprice) + " " + str(self.quant)

    def get_name(self):
        return str(self.porder) + " // " + str(self.supprice) + " // " + str(self.quant)


def get_first_name(self):
    return str(self.username)




User.add_to_class("__str__", get_first_name)


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_name(self):
        return str(self.first_name) + " // " + str(self.last_name) + " // " + str(self.email)