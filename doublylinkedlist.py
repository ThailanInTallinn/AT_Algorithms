class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.inicio = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def insert_first(self, value):
        new_node = DoublyNode(value)
        if self.is_empty():
            self.inicio = self.tail = new_node
        else:
            new_node.next = self.inicio
            self.inicio.prev = new_node
            self.inicio = new_node
        self.length += 1

    def insert_last(self, value):
        new_node = DoublyNode(value)
        if self.is_empty():
            self.inicio = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def delete_first(self):
        if self.is_empty():
            print("Erro: A lista está vazia.")
            return None
        
        removed_value = self.inicio.value
        
        if self.inicio == self.tail: 
            self.inicio = self.tail = None
        else:
            self.inicio = self.inicio.next
            self.inicio.prev = None
            
        self.length -= 1
        return removed_value

    def delete_last(self):
        if self.is_empty():
            print("Erro: A lista está vazia.")
            return None
            
        removed_value = self.tail.value
        
        if self.inicio == self.tail: 
            self.inicio = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            
        self.length -= 1
        return removed_value