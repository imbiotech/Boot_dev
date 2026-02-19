class Stack:
    # __init__ 메서드는 Stack 객체가 생성될 때 호출됩니다.
    # 빈 리스트를 하나 생성해 스택에 저장합니다.
    def __init__(self):
        self.items = []

    # push 메서드는 스택의 최상단 (리스트의 맨 끝)에 새로운 데이터를 추가합니다.
    def push(self, item):
        self.items.append(item)

    # size 메서드는 스택 내에 있는 데이터의 개수를 반환합니다.
    def size(self):
        return len(self.items)

    # peek 메서드는 스택의 최상단에 있는 데이터를 반환합니다.
    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

    # pop 메서드는 스택의 최상단에 있는 데이터를 제거하고 반환합니다.
    def pop(self):
        if not self.items:
            return None
        return self.items.pop()
