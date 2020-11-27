#!usr/bin/env/python3

"""A mixin -
is generally a superclass that is not meant to exist on its own, but is meant to be
inherited by some other class to provide extra functionality"""


class MailSender(object):
	def send_mail(self, message):
		print("Sending mail to " + self.email) # the email will be done by the inheritance
		# Add e-mail logic here

class ContactList(list):
	def search(self, name):
		'''Return all contacts that contain the search value in their name.'''
		matching_contacts = []
		for contact in self: # the class it self
			if name in contact.name:
				matching_contacts.append(contact)
		return matching_contacts

class Contact(object):
	all_contacts = ContactList()

	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.all_contacts.append(self)


# mixins normally works in multiple inheritance
class EmailableContact(Contact, MailSender):  # email is in the contact
	pass


e = EmailableContact("John Smith", "jsmith@example.net")
print(e.send_mail("Hello, test e-mail here")) # mixins at work