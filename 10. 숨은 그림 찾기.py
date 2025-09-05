import sys

di = [ -1,-1,0,1,1,1,0,-1 ]
dj = [ 0,1,1,1,0,-1,-1,-1 ]

def Solve() :
	count = 0
	for i in range(N) :
		for j in range(N) :
			if a[i][j] != X1 : continue
			# X1 발견
			for k in range(8) :
				ni = i + di[k]
				nj = j + dj[k]
				if (ni < 0) or (ni >= N) : continue
				if (nj < 0) or (nj >= N) : continue
				if a[ni][nj] != X2 : continue
				# X2 발견
				ki = ni + di[k]
				kj = nj + dj[k]
				if (ki < 0) or (ki >= N) : continue
				if (kj < 0) or (kj >= N) : continue
				if a[ki][kj] != X3 : continue
				count += 1
	return count

def InputData():
	readl = sys.stdin.readline
	N = int(readl())
	a = [list(map(int,readl().split())) for i in range(N)]
	X1,X2,X3 = map(int, readl().split())

	return N, a, X1, X2, X3

# 입력
# N: 풍경화의 크기
# a: 풍경화
# X1, X2, X3: 숨은 그림을 의미하는 3개의 숫자
N, a, X1, X2, X3 = InputData()
ans = -1

# 코드 작성
ans = Solve()

# 출력
print(ans)





























