from itertools import combinations

# 9명의 난쟁이 키를 입력받음
height = [int(input()) for _ in range(9)]

# 9명의 키 총합 계산
total = sum(height)

# 2명을 뽑는 조합 탐색
for i, j in combinations(height, 2):
    # 나머지 합이 100인지 확인
    if total - (i + j) == 100:
        # 제외할 두 명을 뺀 나머지 7명 출력
        result = [h for h in height if h != i and h != j]
        for h in sorted(result):
            print(h)
        break
