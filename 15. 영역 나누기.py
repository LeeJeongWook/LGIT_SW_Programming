import sys

def InputData():
	readl = sys.stdin.readline
	N = int(readl())
	info = input()
	return N, info

sol = -1

# �Է�
# N: �̵� ������ ����
# info: �̵� ���� ����
N, info = InputData()

# �ڵ� �ۼ�
x = y = 0

dxy = {'0':(1,0),'1':(-1,0),'2':(0,-1),'3':(0,1)}

vertices = {(x,y)}
edges = set()

for c in info:
	dx, dy = dxy[c]
	nx, ny = x + dx, y + dy
	
	edge = tuple(sorted([(x,y),(nx,ny)]))
	edges.add(edge)
	
	vertices.add((nx,ny))
	x, y = nx, ny
	
	E = len(edges)
	V = len(vertices)
	
	sol = E - V + 1
# ���
print(sol)
