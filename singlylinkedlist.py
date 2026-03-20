from typing import final

@final
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None



class SinglyLinkedList:
    def __init__(self):
        self.inicio = None
        
    def add(self, value):
        new_obj = ListNode(value)
        if not self.inicio:
            self.inicio = new_obj
            return

        current_tail = self.inicio
        while current_tail.next:
            current_tail = current_tail.next

        current_tail.next = new_obj
        return

