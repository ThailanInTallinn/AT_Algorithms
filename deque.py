from doublylinkedlist import *
class Deque:
    def __init__(self):
        self.dll = DoublyLinkedList()

    def is_empty(self):
        return self.dll.is_empty()

    def insert_left(self, value):
        self.dll.insert_first(value)

    def insert_right(self, value):
        self.dll.insert_last(value)

    def remove_left(self):
        return self.dll.delete_first()

    def remove_right(self):
        return self.dll.delete_last()

    def peek_left(self):
        if self.is_empty():
            print("Erro: O Deque está vazio.")
            return None
        return self.dll.inicio.value

    def peek_right(self):
        if self.is_empty():
            print("Erro: O Deque está vazio.")
            return None
        return self.dll.tail.value