# 다양한 수로 이루어진 배열이 있을 때, 주어진 수들을 M번 더하여 가장 큰 수를 만들기
# 단, 배역의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다
# --------------------------------------------------------------------------------

# N, M, K 를 공백으로 구분하여 입력받기
print("N, M, K를 입력하세요(공백으로 구분): ")
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
print("N개의 수를 입력하세요(공백으로 구분): ")
data = list(map(int, input().split()))

data.sort() #입력받은 수 정렬(오름차순)
first = data[n-1] #가장 큰 수 
second = data[n-2] #두 번째로 큰 수 

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first 
        m -= 1 
    if m == 0:
        break
    result += second
    m -= 1

print(result)