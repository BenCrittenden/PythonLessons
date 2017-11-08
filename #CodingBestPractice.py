#CodingBestPractice

class Dataset:

	def __init__(self):
		self.data = 'foo'

	def say_hello(self):
		print ('hello')
		print(self.data)


instance = Dataset()
instance.data = 'bar'

#this prints 
#hello
#bar (because the bar overwrites the foo)