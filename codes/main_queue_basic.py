class Queue:
    def __init__(self):
        self.items = []

    # 큐의 가장 마지막에 아이템을 추가합니다.
    def push(self, item):
        self.items = [item] + self.items

    # 큐의 사이즈가 0보다 클 때 가장 첫 원소를 꺼냅니다.
    def pop(self):
        return None if self.size() <= 0 else self.items.pop()

    # 큐의 사이즈가 0보다 클 때 가장 첫 원소를 보여줍니다.
    def peek(self):
        return None if self.size() <= 0 else self.items[-1]

    # 큐의 사이즈를 반환합니다.
    def size(self):
        return len(self.items)
