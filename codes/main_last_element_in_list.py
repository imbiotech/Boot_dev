def last_work_experience(work_experiences):
    # 리스트가 비어있으면 None을 반환합니다.
    if not(work_experiences): 
        return None
    
    # 그 외에는 리스트의 가장 마지막 인덱스를 반환합니다.
    # 파이썬에서는 리스트의 길이를 모를 때 가장 마지막 인덱스를 출력하기 위해 -1을 인덱스로 사용합니다.
    return work_experiences[-1]

    # 또는 한 줄로 표현하면 이렇게 됩니다.
    return work_experiences[-1] if len(work_experiences) > 0 else None
