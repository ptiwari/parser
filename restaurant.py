
class Restaurants(object):
	def __init__(self):
		self.business_hour = {}
		
	@property
	def name(self):
		return self._name
	@name.setter
	def name(self, value):
		self._name = value
