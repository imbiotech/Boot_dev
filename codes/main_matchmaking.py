# python 표준 queue class를 호출하지 않기 위해
# 다른 이름을 사용
from myqueue import Queue

def matchmake(queue, user):
    print(f"Queue items: {queue.items}")
    if (user[-1] == "leave") and (user[0] in queue.items):
        queue.search_and_remove(user[0])
    elif (user[-1] == "join") and (not(user[0] in queue.items)):
        queue.push(user[0])
    if queue.size() >= 4:
        user1 = queue.pop()
        user2 = queue.pop()
        return f"{user1} matched {user2}!"
    else:
        return "No match found"
    return queue
    
