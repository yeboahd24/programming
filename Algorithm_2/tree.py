class Node(object):
	"""Structure for the tree.
	params: left, right and key(data)."""
	def __init__(self, data):
		self.key = data
		self.left = None
		self.right = None

def inorder(temp):
	if not temp:
		return
	inorder(temp.left)
	print(temp.key, end='')
	inorder(temp.right)

def insert(temp, key):
	'''Traversing through the list to find an empty space then insert the key.'''
	q = []
	q.append(temp)
	while len(q):
		temp = q[0] # The root
		q.pop(0)

		# checking if there is no left child.
		if not temp.left:
			temp.left = Node(key)
			break
		q.append(temp.left) # if yes we append it to the list which is q=[].

		if not temp.right:
			temp.right = Node(key)
			break
		q.append(temp.right)

def deleteDeepest(root, d_node):
	q = []
	q.append(root)
	while len(q):
		temp = q.pop(0)
		if temp is d_node:
			temp = None
			return
	if temp.right:
		if temp.right is d_node:
			temp.right = None
			return
		else: q.append(temp.right)
	if temp.left:
		if temp.left is d_node:
			temp.left = None
			return
		else: q.append(temp.left)

def deletion(root, key):
	if root == None:
		return None
	if root.left == None and root.right == None:
		if root.key == key:
			return None
		else: return root
	key_node = None
	q = []
	q.append(root)
	while len(q):
		temp = q.pop(0)
		if temp.data = key:
			key_node = temp
		if temp.left:
			q.append(temp.left)
		if temp.right:
			q.append(temp.right)
	if key_node:
		x = temp.data
		deleteDeepest(root, temp)
		key_node.data = x
	return root



if __name__=='__main__':
	root = Node(20)
	root.left = Node(10)
	root.left.left = Node(12)
	root.right = Node(14)
	root.right = Node(15)
	root.right.left = Node(13)

	print('Inorder traversing before inserting:', end=' ')
	inorder(root)

	key = 12
	insert(root, key)

	print('Inorder traversing after inserting:', end='')
	inorder(root)
