def quick_sort(nums, low=0, high=None):
    # 인덱스에 대한 입력이 없으면, low를 0, high를 가장 마지막 인덱스로 설정
    if high is None:
        high = len(nums) - 1

    # low가 high보다 낮을 때만 정렬이 끝나지 않은 시점이므로 반복문 실행
    if low < high:
        # partition 함수를 통해 자료를 정리하고 중간 지점 인덱스 정보를 받아옴
        middle = partition(nums, low, high)

        # low ~ middle - 1 (왼쪽/앞쪽) 자료를 다시 정렬
        quick_sort(nums, low, middle - 1)
        
        # middle ~ high (오른쪽/뒤쪽) 자료를 다시 정렬
        quick_sort(nums, middle, high)
    return nums

def partition(nums, low, high):
    # pivot을 자료 내 가장 마지막 데이터로 설정
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[j], nums[i] = nums[i], nums[j]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1

