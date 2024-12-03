class Slivik:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.first_element = None
        self.last_element = None

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def append(self, value):
        new_Node = self.Node(value)
        if self.first_element is None:
            self.first_element = new_Node
            self.last_element = new_Node
        else:
            self.last_element.next = new_Node
            self.last_element = new_Node
        self.size += 1

    def recursive_str(self, node):
        if node is None:
            return ""
        next_str = self.recursive_str(node.next)
        if next_str:  # Если есть следующий элемент, добавляем запятую
            return str(node.value) + ", " + next_str
        return str(node.value)

    def __str__(self):
        return "[" + self.recursive_str(self.first_element) + "]"

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        current = self.first_element
        for _ in range(index):
            current = current.next
        return current.value
    
    def append(self, value):
        new_node = self.Node(value)
        if not self.first_element:
            self.first_element = new_node
            return
        current = self.first_element
        while current.next:
            current = current.next
        current.next = new_node

    def sum_indices(self):
        current = self.first_element
        index_sum = 0
        index = 0
        while current:
            index_sum += index * current.value
            current = current.next
            index += 1
        return index_sum

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        if index == 0:
            self.first_element = self.first_element.next
        else:
            current = self.first_element
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1

    def sort(self):
        current = self.first_element
        while current:
            next_node = current.next
            while next_node:
                if current.value > next_node.value:
                    current.value, next_node.value = next_node.value, current.value
                next_node = next_node.next
            current = current.next

myarray = Slivik()
myarray.append(1)
myarray.append(3)
myarray.append(2)
print(myarray)  # [1, 3, 2]
print(myarray)  # 3
#myarray.remove(1)
print(myarray)  # [1, 2]
# [1, 2]