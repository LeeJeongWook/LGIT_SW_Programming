import sys

def InputData():
	readl = sys.stdin.readline
	N = int(readl())
	W = list(map(int, readl().split()))

	return N, W

# 입력 Input
# N: 행성의 수 Number of planets
# W: 행성 질량 Mass of planets
N, W = InputData()
ans = -1

# 코드를 작성 하세요 Write from here
stack = []
ans = 0

for i in W:
	while stack and stack[-1] <= i:
		last = stack.pop()
		if stack and last < i:
			ans += 1
	stack.append(i)
# 출력 Output
ans += (N - 1)
print(ans)
