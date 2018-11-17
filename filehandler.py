import csv
import logging


logger = logging.getLogger(__name__)



		

def read(file_name):		
	logger.debug("Reading File")
	data = [];
	try:
		with open(file_name) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			line_count = 0
			for row in csv_reader:
				data.append(row);
				#print(type(row))
	except IOError:
		logger.debug("IOError")
		print('oops!')
	return data;	
	

