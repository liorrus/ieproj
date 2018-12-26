from polls.models import Product
import csv

def bulkinsert():

    bulk = "C:\\anna\\products.csv"
with open(bulk) as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = Product.objects.get_or_create(pdes=row[0], price=row[1], prep=row[2],)
    return