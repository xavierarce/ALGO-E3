class Stack:
	def __init__(self):
		self._items = []

	def is_empty(self):
		return len(self._items) == 0

	def push(self, value):
		self._items.append(value)

	def pop(self):
		if self.is_empty():
			raise IndexError("Pile vide")
		return self._items.pop()

	def search(self, target):
		return target in self._items


class Queue:
	def __init__(self):
		self._items = []

	def is_empty(self):
		return len(self._items) == 0

	def enqueue(self, value):
		self._items.append(value)

	def dequeue(self):
		if self.is_empty():
			raise IndexError("File vide")
		return self._items.pop(0)

	def search(self, target):
		return target in self._items


class LinkedListNode:
	def __init__(self, value):
		self.value = value
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self, value):
		node = LinkedListNode(value)
		if self.head is None:
			self.head = node
			return

		current = self.head
		while current.next is not None:
			current = current.next
		current.next = node

	def delete(self, value):
		if self.head is None:
			return False

		if self.head.value == value:
			self.head = self.head.next
			return True

		previous = self.head
		current = self.head.next
		while current is not None:
			if current.value == value:
				previous.next = current.next
				return True
			previous = current
			current = current.next

		return False

	def search(self, target):
		current = self.head
		while current is not None:
			if current.value == target:
				return True
			current = current.next
		return False

	def to_list(self):
		values = []
		current = self.head
		while current is not None:
			values.append(current.value)
			current = current.next
		return values
