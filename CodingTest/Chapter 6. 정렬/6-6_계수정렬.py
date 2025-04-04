# ------------------------------------------------------------------------------------------------------------------------
# 계수 정렬 : 데이터의 크기 범위가 제한된 경우 매우 빠르게 정렬할 수 있는 알고리즘
# 데이터의 크기 범위가 제한되어 정수 현태로 표현할 수 있을 때만 사용 가능
# 가장 큰 데이터와 가장 작은 데이터의 차이가 너무 크면 사용할 수 없음
# 왜? 모든 범위를 담을 수 있는 크기의 리스트를 선언해야 하기 때문
# 데이터를 하나씩 확인하며 데이터의 값과 동일한 인덱스의 값을 1씩 증가시키면 계수 정렬이 완료 됨
# 만약 같은 숫자가 2번 이상 나왔다면 인덱스 값이 2 이상으로 올라가게 되고 출력할 때는 인덱스의 값 만큼 해당 숫자를 프린트 하면 됨
# ex) 5가 2번 나왔다면 5번 인덱스의 값은 2이고 출력될 때는 55 이렇게 출력하면 됨
# 계수 정렬은 데이터의 크기가 한정되어 있고 데이터의 크기가 많이 중복되어 있을수록 유리
# ------------------------------------------------------------------------------------------------------------------------

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
# (max(array) + 1) -> 인덱스 번호를 맞추기 위해 최대값보다 1 크게 설정
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 0부터 max(array)까지 반복
    for j in range(count[i]): # 해당 숫자가 등장한 횟수만큼 반복
        print(i, end=' ') # i가 등장한 횟수만큼 출력