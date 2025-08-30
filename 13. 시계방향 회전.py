import sys

def InputData():
	readl = sys.stdin.readline
	R, C = map(int, readl().split())
	Mat = [[int(c) for c in readl().split()] for _ in range(R)]
	return R, C, Mat

# ===========================================
def Rotate(sr, sc, er, ec):
	if sr >= er or sc >= ec:
		return

	a = Mat[sr][sc]

	for r in range(sr + 1, er + 1):
		Mat[r][sc], a = a, Mat[r][sc]
	
	for c in range(sc + 1, ec + 1):
		Mat[er][c], a = a, Mat[er][c]
		
	for r in range(er - 1, sr - 1, -1):
		Mat[r][ec], a = a, Mat[r][ec]
	
	for c in range(ec - 1, sc - 1, -1):
		Mat[sr][c], a = a, Mat[sr][c]
# ===========================================

def Solve():
	n = max(R, C)
	for i in range(n):
		Rotate(0 + i, 0 + i, R - 1 - i, C - 1 - i)

# �Է� �޴� �κ�
# R: ������ ���
# C: ������ ����
# Mat: ���� ������
R, C, Mat = InputData()

# �ڵ� �ۼ�
Solve()
# ����ϴ� �κ�
for r in Mat:
	print(*r)