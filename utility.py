import restaurant as rt
import re

class Parser(object):
	
	def __init__():
		create_patterns();
		self.days_num = {"Sun:0","Mon:1","Tues:2"};
		self.num_days = {"0:Sun","1:Mon","2:Tues"};

	def create_patterns():
		pattern = r"([A-Z][a-z][a-z])\-([A-Z][a-z][a-z])\s+(\d+)\:(\d+)\s+([a|p]m)\s+\-\s+(\d+)\s+([a|p]m)";
		self.pattern_list.append(pattern);
		
	def process_rows(data):
	
		restlist = [];
		for d in data:
			resturnt = rt.Restaurants();
			resturnt.name = d[0];
			add_businees_hour(resturnt,d[1]);
			restlist.append(resturnt);
			print(resturnt.name)



	def add_business_hour(resturnt,date_str):
		match,index = get_match(date_str);
		fill(resturnt,match,index)

	def get_match(date_str):
		match = None
		i = 0
		while i < len(pattern_list):
			match = re.match(pattern_list,date_str);
			if(match is not None):
				break;
		i = i + 1;
		return match,i

	def fill(resturnt,match,index):
		if(index == 0):
			fill_zero_pattern(resturn,match)

	def fill_zero_pattern(resturnt,match):
		open_day = match.group(0);
		close_day = match.group(1);
		open_hr = match.group(2);
		open_min = match.group(3);
		open_ap = match.group(4);
		close_hr = match.group(5);
		close_ap = match.group(6);
		business_hr = bh.BusinessHr(open_hr,open_min,open_ap,close_hr,close_ap)
		i = self.days_num[open_day];
		j = self.days_num[close_day];
		while(i<=j):
			rsturnt[self.num_days[i]] = business_hr;
		
	
