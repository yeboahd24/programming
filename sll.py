class SLLNode:
    """NB SLLNode does not you use previous attribute."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'SLLNode object data:{self.data}'

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class SLL:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return f'SLL object data: {self.head}'

    def is_empty(self):
        return self.head is None

    def add_front(self, new_data):
        temp = SLLNode(new_data)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        siz = 0
        if self.head is None:
            return 0

        current = self.head
        while current is not None:
            current = current.get_next()
            siz +=1
        return siz

    def search(self, data):
        if self.head is None:
            return 'The linked list object is empty.'

        current = self.head
        while current is not None:
            if current.get_data() == data:
                return True
            else:
                current = current.get_data()
            return False

    def remove(self, data):
        if self.head is None:
            return 'No list to remove'
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_data() == None:
                    return 'The value is not present now.'
                else:
                    previous = current
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())




sll = SLL()
node = SLLNode(5)
sll.head = node

#print(sll.is_empty())

nd = SLL()
nd.head
nd.add_front('berry')
#print(nd.head)



#print(node.is_empty()) # this return true because in empty

n = SLL()
n.add_front(1)
n.add_front(2)
n.add_front(3)
#print(n.size())

x = SLL()
x.add_front(1)
x.add_front(2)
#print(x.search(2))

y = SLL()
y.add_front(15)
y.remove(15)
print(y.head)
