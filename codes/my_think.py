from node import Node
from codes.main_linked_list import LinkedList

array = [1, 2, 3]
linked_list = LinkedList()

for el in array:
    new_node = Node(el)

    if linked_list.head is None:
        linked_list.head = new_node
    else:
        prev.next = new_node

    prev = new_node