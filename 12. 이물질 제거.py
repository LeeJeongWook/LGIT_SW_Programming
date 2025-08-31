import math
import sys

def InputData():
	readl = sys.stdin.readline
	N, K = map(int,readl().split())
	X = [int(readl()) for r in range(N)]
	return N, K, X

ans = -1
# �Է� �Լ�
##N : �̹����� ����
##K : ��� �ִ� ��밡�� Ƚ��
##X : �̹����� ��ġ
N, K, X = InputData()
# ���⼭���� �ۼ�
# ===========================================
# ���� Ž��
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