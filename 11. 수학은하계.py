from collections import deque
import sys

def InputData():
	readl = sys.stdin.readline
	S, E1, E2 = map(int, readl().split())
	return S, E1, E2

ans1 = 0
ans2 = 0

# 입력받는 부분
S, E1, E2 = InputData()

arr = [0] * 10000
# 여기서부터 작성
def Prime(n):
	cnt = 0
	for i in range(1, int(n ** 0.5) + 1):
		if n % i == 0:
			cnt += 1
			if i * i != n:
				cnt += 1
	return cnt

for j in range(1000, 10000):
		arr[j] = Prime(j)
	
dist = [-1] * 10000
dist[S] = 0

q = deque([S])

while q:
	cur = q.popleft()
	cur_str = str(cur)
	
	if(dist[E1] != -1) and (dist[E2] != -1):
		break
	
	for i in range(4):
		for digit in '0123456789':
			if cur_str[i] == digit:
				continue
			star_str = cur_str[:i] + digit + cur_str[i+1:]
			star = int(star_str)
			
			if (1000 <= star) and abs(arr[cur] - arr[star]) <= 1:
				if dist[star] == -1:
					dist[star] = dist[cur] + 1
					q.append(star)
		
# 출력하는 부분
print(dist[E1])
print(dist[E2])
