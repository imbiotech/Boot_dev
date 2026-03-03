class Node:
    # 최초의 값을 val에 삽입합니다.
    # 최초 next는 None으로 설정합니다.
    def __init__(self, val):
        self.val = val
        self.next = None

    # next가 주어지면 next를 해당 node로 대체합니다.
    def set_next(self, node):
        self.next = node

    # don't touch below this line

    def __repr__(self):
        return self.val
