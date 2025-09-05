import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	map_area = [list(readl().strip()) for _ in range(N)]
	return N, map_area

#구매자 이름 Buyer's name
ans = ""
#구매자 영역 개수 Number of buyer's area
areacnt = 0

# 입력 받는 부분 Input
N, map_area = Input_Data()

# 여기서부터 작성 Write from here
def bfs(sr, sc, color, visited):
	q = deque()
	q.append((sr, sc))
	visited[sr][sc] = True
	cnt = 1
	
	di = [(0,1), (0,-1), (-1,0), (1,0)]
	
	while q:
		r, c = q.popleft()
		for dr, dc in di:
			nr, nc = r + dr, c + dc
			if 0 <= nr < N and 0 <= nc < N:
				if not visited[nr][nc] and map_area[nr][nc] == color:
					visited[nr][nc] = True
					q.append((nr,nc))
					cnt += 1
					
	return cnt
				
area = {"R":0, "G":0, "B":0}
grid = {"R":0, "G":0, "B":0}
visited = [[False] * N for _ in range(N)]

for i in range(N):
	for j in range(N):
		if not visited[i][j]:
			color = map_area[i][j]
			area[color] += 1
			cnt = bfs(i, j, color, visited)
			grid[color] += cnt

prior = {"R":2, "G":1, "B":0}
data = []
for col in ["R", "G", "B"]:
	data.append((area[col], grid[col], col))
data.sort(key=lambda x : (-x[0], -x[1], -prior[x[2]]))

ans = data[0][2]
areacnt = data[0][0]
# 출력하는 부분 Output
print(ans, areacnt)




























