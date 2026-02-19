from stack import Stack


def is_balanced(input_str):
    # 새 Stack 생성
    stack = Stack()

    # 입력된 문자열을 순차적으로 스택에 쌓습니다.
    for t in input_str:
        stack.push(t)
    
    # 스택을 가장 위쪽부터 순차적으로 출력하면서 괄호의 밸런스가 맞는지를 검증합니다.
    count = 0
    while stack.size() > 0:
        # 닫는 괄호는 +1, 여는 괄호는 -1을 부여합니다.
        if stack.pop() == ")":
            count += 1
        else:
            count -= 1
        
        # 만약 수치가 음수로 내려간다면, 닫는 괄호 없이 여는 괄호가 먼저 있다는 것을 뜻하고, 
        # 이미 밸런스 맞지 않습니다. 거짓을 반환합니다.
        if count < 0:
            return False
    
    # 수치가 0보다 크면 밸런스가 맞지 않다는 의미입니다.
    if count > 0:
        return False
    return True
