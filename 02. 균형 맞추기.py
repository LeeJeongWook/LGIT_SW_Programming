import sys

def InputData():
	readl = sys.stdin.readline
	N = int(readl())
	Box = [list(map(int, readl().split())) for r in range(N)]
	return N, Box


ans = -1
# 입력 함수
##N : 상자의 크기

N, Box = InputData()
# 여기서부터 작성
boxes = []
for i in range(N):
	box = 0
	for j in range(N):
		box += Box[i][j]
	boxes.append(box)
	
for j in range(N):
	box = 0
	for i in range(N):
		box += Box[i][j]
	boxes.append(box)

max_box = max(boxes)

for i in boxes:
	ans += max_box - i
"""
row = [sum(i) for i in Box]
col = [sum(i) for i in zip(*Box)]
arr = row + col
ans = (max(arr) * N) - sum(row)
"""
# 출력
print(ans)
