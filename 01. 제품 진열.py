import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	ID = list(map(int, readl().split()))
	return N, ID

def CalLargestBlock(id_ignore):
	max_block_size = 0
	tmp_arr = []
	cur_size = 1
	
	for i in ID:
		if i != id_ignore:
			tmp_arr.append(i)
			
	for i in range(1, len(tmp_arr)):
		if tmp_arr[i] == tmp_arr[i - 1]: cur_size += 1
		else: cur_size = 1

		if max_block_size < cur_size: max_block_size = cur_size
	
	return max_block_size
"""
def CalLargestBlock(id_ignore):
	max_block_size = 0
	cur_size = 1
	tmpID = [i for i in ID if i != id_ignore] #<<<
	for i in range(1, len(tmpID)): #<<<
		if tmpID[i] == tmpID[i - 1]: cur_size += 1 #<<<
		else: cur_size = 1

		if max_block_size < cur_size: max_block_size = cur_size
	return max_block_size
"""
def Solve():
	max_cnt = 0
	sol = 10000000
	for i in range(N):
		ret = CalLargestBlock(ID[i])
		if (max_cnt < ret) or ((max_cnt == ret) and (sol < ID[i])):
			max_cnt = ret
			sol = ID[i]
	return sol

# 입력 받는 부분
N, ID = Input_Data()

ans = Solve()

# 출력하는 부분
print(ans)
