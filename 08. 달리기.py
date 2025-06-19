import sys

def Input_Data():
	readl = sys.stdin.readline
	N, T = map(int, readl().split())
	l = [list(map(int, readl().split())) for n in range(N)]
	P, S = [list(x) for x in zip(*l)]
	return N, T, P, S


# 입력 Input
# N : 선수의 인원수 number of playersnumber of players
# T : 시간 time
# P : 선수 초기 위치 player initial position
# S : 선수 속도 player speed
# group_first :각 그룹의 선두선수 leader of each group
N, T, P, S = Input_Data()
ans = 0
group_first = []
# 코드를 작성하세요 Write the code
arr = []
for i in range(N):
	arr.append(S[i] * T + P[i])
	
for i in range(N-1, -1, -1):
	if not group_first or tmp > arr[i]:
		tmp = arr[i]
		ans += 1
		group_first.append(i+1)

# 출력 Output
print(ans)
print(*group_first, sep=' ', end=' ')
