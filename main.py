from node import Node

class LinkedList:
    # 최초의 연결 리스트는 빈 head 자리만 가진 상태로 시작합니다.
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # don't touch below this line

    def __repr__(self):
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(current.val)
            current = current.next
        return " -> ".join(nodes)
