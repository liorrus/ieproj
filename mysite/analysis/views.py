from django.shortcuts import render
import schedule
import time
import csv
from datetime import date


def get_filename_datetime():
	return "file-" + str(date.today()) + ".csv"


def Report():
	# write output to csv
	# name the file as today's date and time
	# need to test if naming works


	# Get full path for writing.
	name = get_filename_datetime()
	path = "C:\\anna\\" + name

	myFile = time.strftime("%Y%m%d-%H%M%S")

	result = cur.fetchall()

	# Getting Field Header names
	column_names = [i[0] for i in cur.description]
	fp = open(path, 'w')
	myFile = csv.writer(fp, lineterminator='\n')  # use lineterminator for windows
	myFile.writerow(column_names)
	myFile.writerows(result)
	fp.close()


Report()
"""
schedule.every().sunday.at("06:00").do(Report)

while True:
	schedule.run_pending()
	time.sleep(1)
	"""

"""
	https://stackoverflow.com/questions/4613465/using-python-to-write-mysql-query-to-csv-need-to-show-field-names
	https://stackoverflow.com/questions/10607688/how-to-create-a-file-name-with-the-current-date-time-in-python
"""