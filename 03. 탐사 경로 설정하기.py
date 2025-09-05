from collections import deque

import sys

def Input_Data():
	readl = sys.stdin.readline
	R, C = map(int,readl().split())
	map_city = [readl().strip() for _ in range(R)]
	return R, C, map_city


sol = -1
# 입력 받는 부분
R, C, map_city = Input_Data()

# 여기서부터 작성
INF = 10**9

def bfs(sr, sc, R, C, grid):
	dist = [[-1] * C for _ in range(R)] # -1로 초기화
	dist[sr][sc] = 0 # 시작점
	q = deque()
	q.append((sr, sc))
	directions = [(-1,0), (1, 0), (0, -1), (0, 1)]
	
	while q:
		r, c = q.popleft()
		for dr, dc in directions:
			nr, nc = r + dr, c + dc
			if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '*' and dist[nr][nc] == -1:
				dist[nr][nc] = dist[r][c] + 1
				q.append((nr, nc))
				
	return dist

points_dict = {}
start = None

for r in range(R):
	for c in range(C):
		pos = map_city[r][c]
		if pos == 'S':
			start = (r, c)
		elif pos.isdigit():
			digit = int(pos)
			points_dict[digit] = (r, c)

sorted_digits = sorted(points_dict.keys()) # 순서대로 방문할 인덱스
points = [start] + [points_dict[i] for i in sorted_digits]
n = len(points) # 전체 방문지점 수


dist_matrix = [[INF] * n for _ in range(n)]

for i in range(n):
	sr, sc = points[i]
	dist2d = bfs(sr, sc, R, C, map_city)
	for j in range(n):
		tr, tc = points[j]
		d = dist2d[tr][tc]
		# print(f'tr:{tr}, tc:{tc}, d:{d}')
		if d != -1:
			dist_matrix[i][j] = d
	# print()			
	# for d in dist_matrix:
	# 	print(d)

dp = [[INF] * n for _ in range(1 << n)]
dp[1 << 0][0] = 0

for mask in range(1 << n):
	for i in range(n):
		if dp[mask][i] == INF:
			continue
		for j in range(n):
			if(mask & (1 << j)) == 0:
				nxt_mask = mask | (1 << j)
				new_cost = dp[mask][i] + dist_matrix[i][j]
				if new_cost < dp[nxt_mask][j]:
					dp[nxt_mask][j] = new_cost
		for d in dp:
			print(d)
		print()

full_mask = (1 << n) -1
ans = INF
for i in range(n):
	cost = dp[full_mask][i] + dist_matrix[i][0]
	if cost < ans:
		ans = cost
	
# 출력하는 부분
print(ans)




























