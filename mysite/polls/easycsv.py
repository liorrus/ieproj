from my_projects.models import Person
from adaptor.model import CsvDbModel

class MyCsvModel(CsvDbModel):

     class Meta:
        dbModel = Order
        delimiter = ","


# my_csv_list = MyCsvModel.import_data(data = open("my_csv_file_name.csv"))

