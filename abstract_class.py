class Hack:
	'''This abstract method even works
	if one of the abstract methods is
	implemented'''
	def email_Hack(self):
		raise NotImplementedError()  # This kind of abstraction is not good

	def fb_Hack(self):
		raise  NotImplementedError()


class Pack(Hack):
	def email_Hack(self):
		print('Email hacking')  #Like this one only the email_Hack is define but there won't be no errors.


# p = Pack()
# print(p.email_Hack())


from abc import  ABCMeta,abstractmethod

class Fb_Hack(metaclass=ABCMeta):
	'''This abstract method display errors if any of the instance method is not define'''

	@abstractmethod
	def password(self):
		pass

	@abstractmethod
	def email(self):
		pass

class Checking(Fb_Hack):
	def password(self):
		print('Password hacking...')  # There will be an error because email instance is not define
c = Checking()
print(c.password())


