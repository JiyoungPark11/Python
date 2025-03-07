# --------------------------------------------------
# 1. 첫째 줄에 수열에 속해 있는 개수 n 입력받음
# 2. 둘째 줄부터 n+1번째 줄까지 n개의 수를 입력받음
# 3. 입력받은 수를 내림차순 정렬
# --------------------------------------------------

n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

print(array)