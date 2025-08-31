import math
import sys

def InputData():
	readl = sys.stdin.readline
	N, K = map(int,readl().split())
	X = [int(readl()) for r in range(N)]
	return N, K, X

ans = -1
# 입력 함수
##N : 이물질의 개수
##K : 장비 최대 사용가능 횟수
##X : 이물질의 위치
N, K, X = InputData()
# 여기서부터 작성
# ===========================================
# 이진 탐색
sorted_X = sorted(X)

def check(v):
    count = 1
    last_position = sorted_X[0] + (2 * v)
    
    for i in range(1, len(sorted_X)):
        if sorted_X[i] > last_position:
            count += 1
            last_position = sorted_X[i] + (2 * v)
    
    return count

left, right = 1, sorted_X[-1]
result = right

while left <= right:
    mid = (left + right) // 2
    
    if check(mid) <= K:
        result = mid
        right = mid - 1
    else:
        left = mid + 1
    print(left,right)

print(result)
# ===========================================