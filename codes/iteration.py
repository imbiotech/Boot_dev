def create_message_generator():
    yield "hi"
    yield "there"
    yield "friend"

gen = create_message_generator()

# 처음 함수를 호출하면
first = next(gen)
print(first)
# 'hi'가 출력되고, 해당 부분에 함수는 멈춰있습니다.

# 두 번째로 함수를 호출하면
second = next(gen)
print(second)  
# 'there'이 출력되고, 해당 부분에 함수는 멈춰있습니다.

# 세 번째로 함수를 호출하면
third = next(gen)
print(third)  
# 'friend'가 출력되고 함수는 종료됩니다.

gen2 = create_message_generator()

for message in gen2:
    print(message)