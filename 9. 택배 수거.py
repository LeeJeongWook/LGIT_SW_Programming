import sys

from itertools import combinations, permutations

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl()) # 택배 수거 지점 수 Number of parcels collection points
	base = [list(map(int,readl().split())) for _ in range(2)] # 택배 영업소 위치 입력 Parcels office location
	pos = [list(map(int,readl().split())) for _ in range(N)] # 택배 수거지점 위치 입력 Parcels collection point location
	return N, base, pos

ans = -1
# 입력 받는 부분 Input
N, base, pos = Input_Data()

# 여기서 부터 작성 Write the code
def get_cost(p1, p2, box_cnt):
	return (abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])) * (1 + box_cnt)

def route_cost(base, route):
	cost = 0
	box_cnt = 0
	cur_pos = base
	
	for p in route:
		cost += get_cost(cur_pos, p, box_cnt)
		box_cnt += 1
		cur_pos = p
		
	cost += get_cost(cur_pos, base, box_cnt)
	return cost

ans = float('inf')
all_indices = range(N)

for sizeA in range(N + 1):
	for subsetA in combinations(all_indices, sizeA):
		subsetB = [i for i in all_indices if i not in subsetA]
		pointsA = [pos[i] for i in subsetA]
		bestA = float('inf')
		
		if not pointsA:
			bestA = 0
		else:
			for permA in permutations(pointsA):
				costA = route_cost(base[0], permA)
				if costA < bestA:
					bestA = costA
					
		pointsB = [pos[i] for i in subsetB]
		bestB = float('inf')

		if not pointsB:
			bestB = 0
		else:
			for permB in permutations(pointsB):
				costB = route_cost(base[1], permB)
				if costB < bestB:
					bestB = costB
				
				
		total_cost = bestA + bestB
		if total_cost < ans:
			ans = total_cost
		
# 출력 하는 부분 Output
print(ans) 
