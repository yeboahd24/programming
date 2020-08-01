from collections import UserList

class ExtendList(UserList):
	def __setitem__(self, i, value):
		if i==len(self.data):
			self.data.append(value)
		else:
			self.data[i] = value

l = ExtendList()
for i in range(10):
	l[i] = i
print(l)