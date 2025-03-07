n = 1260
count = 0

coin_type = [500, 100, 50, 10]

for coin in coin_type:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin # 나머지 거스름돈 구하기

print(count)