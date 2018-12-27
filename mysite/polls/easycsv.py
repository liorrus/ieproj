from adaptor.model import CsvDbModel
from polls.models.py import Order

class MyCsvModel(CsvDbModel):

     class Meta:
        dbModel = Order
        delimiter = ","
        has_header = 1


my_csv_list = MyCsvModel.import_data(data = open("1000randomorders.csv"))