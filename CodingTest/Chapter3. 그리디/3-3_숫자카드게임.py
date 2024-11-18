# 목표 : 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 것
# 아이디어 : 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수를 찾는다
# -------------------------------------------------------------------------

# N, M을 공백으로 구분하여 입력받기
print("N * M 행렬의 크기를 입력하세요(공백으로 구분): ")
n, m = map(int, input().split())

result = 0
# Ver1. min()함수 사용-------------------------------------------
for i in range(n):
    data = list(map(int, input().split()))
    min_val = min(data)
    result = max(result, min_val)

print(result)

# Ver2. 이중 반복문 사용-------------------------------------------
# for i in range(n):
#     data = list(map(int, input().split()))
#     min_val = 10001
#     for a in data:
#         min_val = min(min_val, a)
#     result = max(result, min_val)

# print(result)