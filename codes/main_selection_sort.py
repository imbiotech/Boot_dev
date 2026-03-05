def selection_sort(nums):
    n = len(nums)
    # 모든 원소를 순차적으로 순회
    for i in range(n):
        # 현재 인덱스를 가장 작은 숫자로 설정하고
        smallest_idx = i
        # 현재 인덱스 이후의 원소를 돌면서
        for j in range(i + 1, n):
            # 현재 인덱스 숫자보다 작으면 해당 숫자를 가장 작은 숫자로 설정
            if nums[i] > nums[j]:
                smallest_idx = j
        # 한 번의 순회마다 한 번의 교환만 진행
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
    return nums


