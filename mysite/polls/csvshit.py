from adaptor.model import CsvModel
class MyCSvModel(CsvModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # costumer ID
    orderDate = models.DateTimeField()
    orderPick = models.DateTimeField()
    ORDER_STATUS = 'T'


    class Meta:
         delimiter = ","
         dbModel = Order