class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def __len__(self):
        return self._length

    def insert(self, index, value):
        if index < 0 or index > self._length:
            raise IndexError("Индекс выходит за пределы списка")
            
        new_node = Node(value)
        
        if self._length == 0:
            self.head = self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif index == self._length:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            if index < self._length // 2:
                current = self.head
                for _ in range(index):
                    current = current.next
            else:
                current = self.tail
                for _ in range(self._length - index - 1):
                    current = current.prev
            
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node
            
        self._length += 1

    def get(self, index):
        if index < 0 or index >= self._length:
            raise IndexError("Индекс выходит за пределы списка")
            
        if index < self._length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self._length - index - 1):
                current = current.prev
        return current.value

    def delete(self, index):
        if index < 0 or index >= self._length:
            raise IndexError("Индекс выходит за пределы списка")
            
        if index < self._length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self._length - index - 1):
                current = current.prev

        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next
            
        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev
            
        self._length -= 1
        return current.value
