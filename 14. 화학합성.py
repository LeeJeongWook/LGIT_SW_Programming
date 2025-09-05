import sys

def InputData():
	readl = sys.stdin.readline
	N, M = map(int,readl().split())
	ID = list(map(int,readl().split()))
	return N, M, ID

ans = 0
# 입력 함수
N, M, ID = InputData()

def max_count(cnt_ID):
	max_cnt = 0
	for j in range(16):
		cnt = cnt_ID[j]
		if j > 0:
			cnt += cnt_ID[j-1]
		if j < 15:
			cnt += cnt_ID[j+1]
		if max_cnt < cnt:
			max_cnt = cnt
	return max_cnt

cnt_ID = [0] * 16
for i in range(M):
	cnt_ID[ID[i]] += 1
	
ans = max_count(cnt_ID)

left = 0
for right in range(M,N):
	cnt_ID[ID[left]] -= 1
	cnt_ID[ID[right]] += 1
	
	current = max_count(cnt_ID)
	if ans < current:
		ans = current
	left += 1

# 출력하는 부분
print(ans)




























