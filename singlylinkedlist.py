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
        new_obj.index = self.length
        self.tail = new_obj

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
        self.length += 1
        return

    def search(self, value):
        curr_node = self.inicio
        while curr_node:
            if(curr_node.value == value):
                return curr_node
            curr_node = curr_node.next
        print("Item não encontrado.", end="\n\n")
        return -1

    def delete(self, value):
        item = self.search(value)
        if(item == -1):
           print(f"Falha na deleção: valor não encontrado", end="\n\n")
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
        self.tail = curr_node
        self.length -= 1
        return 1

    def insert_at(self, index, value):
        if index < 0:
            print("Erro: index menor que 0", end="\n\n")
            return -1
        elif index > self.tail.index:
            self.insert_last(value)
            return 1

        curr_node = self.inicio
        while curr_node:
            if(curr_node.next.index == index):
                break
            curr_node = curr_node.next

        new_obj = ListNode(value)
        new_obj.index = index
        new_obj.next = curr_node.next
        curr_node.next = new_obj
        pointer = new_obj.next
        while pointer:
            if pointer.next is None:
                self.tail = pointer
            pointer.index += 1
            pointer = pointer.next
        self.length += 1
        return 1
        
    def delete_at(self, index):
        if index < 0:
            print("Erro: index menor que 0", end="\n\n")
            return -1
        elif index > self.tail.index:
            index = self.tail.index

        pointer = self.inicio
        while pointer:
            if pointer.next.index == index:
                break
            pointer = pointer.next

        pointer.next = pointer.next.next
        pointer = pointer.next
        while pointer:
            if pointer.next is None:
                self.tail = pointer
            pointer.index -= 1
            pointer = pointer.next
        self.length -= 1
        return 1

    def exibir(self):
        pointer = self.inicio
        while pointer:
            print(f"Index: {pointer.index} | Valor: {pointer.value}")
            pointer = pointer.next

    def __str__(self):
        if self.__len__() == 0:
            print("Lista vazia", end="\n\n")
            return -1

        pointer = self.inicio
        while pointer:
            print(f"{pointer.value}->", end=" ")
            pointer = pointer.next
