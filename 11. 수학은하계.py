import sys
from collections import deque

def InputData():
	readl = sys.stdin.readline
	S, E1, E2 = map(int, readl().split())
	return S, E1, E2

# 입력받는 부분
S, E1, E2 = InputData()

div_count = [0] * 10000

for num in range(1000, 10000):
	cnt = 0
	i = 1
	while i * i <= num:
		if num % i == 0:
			cnt += 1
			if i != (num // i):
				cnt += 1
		i += 1
		div_count[num] = cnt

dist = [-1] * 10000
dist[S] = 0

q = deque([S])
while q:
	cur = q.popleft()
	print(cur)
	if(dist[E1] != -1) and (dist[E2] != -1):
		break
	
	cur_str = str(cur)
	
	for i in range(4):
		for digit in '0123456789':
			if cur_str[i] == digit:
				continue
			
			candidate_str = cur_str[:i] + digit + cur_str[i+1:]
			candidate = int(candidate_str)
			
			if(candidate >= 1000) and abs(div_count[cur] - div_count[candidate]) <= 1:
				if dist[candidate] == -1:
					dist[candidate] = dist[cur] + 1
					q.append(candidate)

print(dist[E1])
print(dist[E2])
