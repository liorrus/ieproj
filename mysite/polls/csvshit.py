from adaptor.model import CsvModel
class MyCSvModel(CsvModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # costumer ID
    orderDate = models.DateTimeField()
    orderPick = models.DateTimeField()
    ORDER_STATUS = 'T'


    class Meta:
         delimiter = ","
         dbModel = Order

############
############

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
    ifSupplied = models.BooleanField(default=True)
    product1 = models.ForeignKey(Product, null=False, on_delete=models.CASCADE, related_name="pro1")  # product ID
    product2 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="pro2", default=52)  # product ID
    product3 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="pro3", default=52)  # product ID
    extra1 = models.ForeignKey(NewExtra, on_delete=models.CASCADE, related_name="ex1", default=3)  # extra1 if have
    extra2 = models.ForeignKey(NewExtra, on_delete=models.CASCADE, related_name="ex2", default=3)  # extra2 if have
    extra3 = models.ForeignKey(NewExtra, on_delete=models.CASCADE, related_name="ex3", default=3)  # extra3 if have
    extra4 = models.ForeignKey(NewExtra, on_delete=models.CASCADE, related_name="ex4", default=3)  # extra4 if have
    extra5 = models.ForeignKey(NewExtra, on_delete=models.CASCADE, related_name="ex5", default=3)  # extra5 if have
    component1 = models.ForeignKey(Components, on_delete=models.CASCADE, related_name="comp1", default=6)  # component1 if have
    component2 = models.ForeignKey(Components, on_delete=models.CASCADE, related_name="comp2", default=6)  # component2 if have
    component3 = models.ForeignKey(Components, on_delete=models.CASCADE, related_name="comp3", default=6)  # component3 if have
    component4 = models.ForeignKey(Components, on_delete=models.CASCADE, related_name="comp4", default=6)  # component4 if have
    component5 = models.ForeignKey(Components, on_delete=models.CASCADE, related_name="comp5", default=6)  # component5 if have

"""