# ---------------------------------------------------------------------------
# 어떤 수 N이 1이 될 때까지 다음 두 과정 중 하나를 반복적으로 선택하여 수행한다.
# 단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다
# 1. N에서 1을 뺀다
# 2. N을 K로 나눈다
# ---------------------------------------------------------------------------

print("N과 K를 입력하세요(공백으로 구분): ")
n, k = map(int, input().split())

result = 0

while n >= k:
    while n % k != 0: # n이 k 이상이라면 k로 나누기
        n -= 1
        result += 1
    n //= k # k로 나누기
    result  += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)

