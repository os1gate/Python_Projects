class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Очередь
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def put(self, data):
        new_node = Node(data)

        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.size += 1

    def get(self):
        if self.first is None:
            print("Очередь пуста")
            return None

        data = self.first.data
        self.first = self.first.next

        if self.first is None:
            self.last = None

        self.size -= 1
        return data

    def isempty(self):
        return self.size == 0

    def show(self):
        current = self.first

        while current:
            print(current.data, end=" ")
            current = current.next

        print()


# Стек
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.top is None:
            print("Стек пуст")
            return None

        data = self.top.data
        self.top = self.top.next
        self.size -= 1

        return data

    def isempty(self):
        return self.size == 0

    def show(self):
        current = self.top

        while current:
            print(current.data, end=" ")
            current = current.next

        print()


# Дека
class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_front(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.size += 1

    def push_back(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def pop_front(self):
        if self.head is None:
            print("Дека пуста")
            return None

        data = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self.size -= 1
        return data

    def pop_back(self):
        if self.head is None:
            print("Дека пуста")
            return None

        if self.head == self.tail:
            data = self.head.data
            self.head = None
            self.tail = None
            self.size -= 1
            return data

        current = self.head

        while current.next != self.tail:
            current = current.next

        data = self.tail.data
        self.tail = current
        self.tail.next = None

        self.size -= 1
        return data

    def isempty(self):
        return self.size == 0

    def show(self):
        current = self.head

        while current:
            print(current.data, end=" ")
            current = current.next

        print()


# Проверка

q = Queue()
q.put(1)
q.put(2)
q.put(3)
q.show()
print("Удалено:", q.get())
q.show()

print()

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.show()
print("Удалено:", s.pop())
s.show()

print()

d = Deque()
d.push_front(5)
d.push_back(10)
d.push_back(15)
d.show()
print("Удалено спереди:", d.pop_front())
print("Удалено сзади:", d.pop_back())
d.show()
