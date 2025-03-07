# ----------------------------------------------------------------------------------------------------
# 퀵 정렬
# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 스왑 후 리스트트 반으로 나누기
# 피벗 사용 : 큰 숫자와 작은 숫자를 교환할 때, 교환 하기 위한 기준
# 호어 분할 : 리스트에서 첫 번째 데이터를 피벗으로 정함
# 호어 분할 이후에는 피벗 기준으로 왼쪽은 피벗보다 작은 데이터, 오른쪽은 피벗보다 큰 데이터로 정렬됨
# 이 후에 왼쪽, 오른쪽 각각 정렬 방식은 이전과 같이 진행(호어분할 후 정렬)
# 재귀 함수로 구현하면 간결함
# 퀵 정렬이 끝나는 조건 = 현재 리스트의 데이터 개수가 1개인 경우
# 호어 분할을 택하는 경우, 삽입 정렬과 반대로 이미 데이터가 정렬되어 있는 경우 매두 느리게 동작
# ----------------------------------------------------------------------------------------------------

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 1. 기본 구현
# def quick_sort(array, start, end):
#     if start >= end: # 원소가 1개인 경우 정렬됐다고 보고 종료
#         return
#     pivot = start # 피벗은 첫번째 원소
#     left = start + 1 # 피벗보다 큰 값을 찾기 위한 왼쪽 포인터
#     right = end # 피벗보다 작은 값을 찾기 위한 오른쪽 포인터
# 
#     while left <= right: 
#         while left <= end and array[right] <= array[pivot]: # 피벗보다 큰 데이터를 찾을 때까지 left 이동
#             left += 1
#         while right > start and array[right] >= array[pivot]: # 피벗보다 작은 데이터를 작을 때까지 right 이동
#             right += 1
#         if left > right: # 포인터가 엇갈린 경우, 피벗과 작은 값을 교체
#             array[right], array[pivot] = array[pivot], array[right]
#         else: # 엇갈리지 않았다면, 작은 데이터와 큰 데이터를 교체
#             array[left], array[right] = array[right], array[left]
# 
#     # 분할 후, 왼쪽과 오른쪽 부분을 각각 정렬(재귀 호출)
#     quick_sort(array, start, right-1)
#     quick_sort(array, right+1, end)
# 
# quick_sort(array, 0, len(array)-1)
# print(array)

# 2. 파이썬 장점을 살린 퀵 정렬 소스코드
def quick_sort(array):
    if len(array) <= 1: # 리스트가 1개 이하 원소만 담고 있다면 종료
        return array
    
    pivot = array[0] # 피벗은 첫번째 요소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 리스트
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 리스트

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))