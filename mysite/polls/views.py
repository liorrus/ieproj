from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


import pymysql.cursors
# Connect to the database

def index(request):
    connection = pymysql.connect(host='35.225.130.71',
                                user='root',
                                password='ShushTush2018',
                                db='ANNA',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `PDES`, `UNIT` FROM `PARTS` WHERE `PDES`=%s"
            cursor.execute(sql, ('מפיות',))
            result = cursor.fetchone()
            
    return HttpResponse(str("Hi \n You're id is " + str(result['PDES']) + " and password is " + str(result['UNIT'])))
    