from typing import final

@final
class ListNode:
    def __init__(self, value):
        self.value = value
        self.index = 0
        self.next = None



class SinglyLinkedList:
    def __init__(self):
        self.inicio = None
        self.tail = None
        self.length = 0
        
    def insert_last(self, value):
        new_obj = ListNode(value)
        self.tail = new_obj
        new_obj.index = self.length

        if not self.inicio:
            self.inicio = new_obj
            self.length += 1
            return

        current_tail = self.inicio
        while current_tail.next:
            current_tail = current_tail.next

        current_tail.next = new_obj
        self.length += 1
        return

    def __len__(self):
        return self.length

    def insert_first(self, value):
        if not self.inicio:
            self.insert_last(value)
            return
        
        new_obj = ListNode(value)
        new_obj.index = 0
        new_obj.next = self.inicio 
        self.inicio = new_obj
        curr_node = new_obj.next
        while curr_node:
            curr_node.index += 1
            curr_node = curr_node.next
        return

    def search(self, value):
        curr_node = self.inicio
        while curr_node:
            if(curr_node.value == value):
                return curr_node
            curr_node = curr_node.next
        print("Item não encontrado.")
        return -1

    def delete(self, value):
        item = self.search(value)
        if(item == -1):
           print(f"Falha na deleção: valor não encontrado")
           return -1
        curr_node = self.inicio
        while curr_node:
            if curr_node.next.value == value:
                break
            curr_node = curr_node.next

        curr_node.next = item.next if item.next else None
        
        while curr_node.next:
            curr_node.next.index -= 1
            curr_node = curr_node.next
        return 1


