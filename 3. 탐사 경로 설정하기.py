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
dest = {}

for i in range(R):
	for j in range(C):
		pos = map_city[i][j]
		if pos == 'S':
			start = (i, j)
		elif pos.isdigit():
			digit = int(pos)
			dest[digit] = (i, j)
			
sorted_dest = sorted(dest.keys())
point = [start] + [dest[i] for i in sorted_dest]
n = len(point)

dist = [[INF] * n for i in range(n)]

for i in range(n):
	sr, sc = point[i]
	dist = bfs
		
# 출력하는 부분
# print(sol)
