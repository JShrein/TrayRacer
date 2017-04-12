from abc import ABCMeta, abstractmethod

class stuff(metaclass=ABCMeta):
	@abstractmethod
	def doit(self, num):
		pass

class ball(stuff):
	def doit(self, num):
		print('bounced ' + str(num) + ' times')

b = ball()
b.doit(5)
