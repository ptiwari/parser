import sys
import filehandler as fh
import datetime as dt
import settings as st
import utility as ut

class ProcessQuery(object):

	def get_open_restaurants(self, date):
		print("Test")
	
	#def 

	def main(self):
		if(len(sys.argv)<2):
			print("Wrong argument format.Python3 restaurants.py <Input_File_Name>.");
			return;
		file_name = sys.argv[1];
		data = fh.read(file_name)
		ut.process_rows(data)
		#dt.datetime.strptime("Mon 10:40PM","%a %I:%M%p")
		date = dt.datetime.strptime(st.TIMESTR,st.FORMAT)

if __name__== "__main__":
	pq = ProcessQuery()
	pq.main()

		
