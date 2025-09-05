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
X.sort()

def is_cover(V):
	used = 0
	i = 0
	
	while i < N:
		used += 1
		if used > K:
			return False

		limit = X[i] + (2 * V)
		print(limit, end = ' ')
		while(i < N) and (X[i] <= limit):
			i += 1
			
	return True

low, high = 0, X[-1] - X[0]
ans = high

while low <= high:
	mid = (low + high) // 2
	if is_cover(mid):
		ans = mid
		high = mid - 1
	else:
		low = mid + 1
	
# ���
print(ans)




























