# 데이터 입력 받기
def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	ID = list(map(int, readl().split()))
	return N, ID

# 데이터 초기화
arr = [0 for _ in range(5)]
table = [[0] * 5 for _ in range(5)]

# 문자열 자르기, 합치기
my_str = "apple,banana,cherry"
my_str = my_str.split(',')
# Output: ['apple', 'banana', 'cherry']

words = ['apple', 'banana', 'cherry']
words = " ".join(words)
# Output: apple banana cherry

# 테이블 열, 행의 합 구하기
row = [sum(i) for i in table]
col = [sum(i) for i in zip(*table)]

# 정렬

nums = [5, 2, 9, 1]
sorted_nums = sorted(nums)
# Output: [1, 2, 5, 9]
print(sorted(nums, reverse=True))
# Output: [9, 5, 2, 1]

# Lamda Ex
words = ['banana', 'apple', 'cherry', 'kiwi']
words.sort(key=lambda x: len(x))
sorted_words = sorted(words, key=lambda x: len(x))
# Output: ['kiwi', 'apple', 'banana', 'cherry']

prior = {"R":2, "G":1, "B":0}
data = []
for col in ["R", "G", "B"]:
	data.append((area[col], grid[col], col))
data.sort(key=lambda x : (-x[0], -x[1], -prior[x[2]]))

# DFS
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for next in graph[v]:
        if not visited[next]:
            dfs(graph, next, visited)

# BFS
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        for next in graph[v]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True

# 순열
from itertools import permutations

data = [1, 2, 3]
result = list(permutations(data, 2))
print(result)
# Output: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# 조합
from itertools import combinations

data = [1, 2, 3]
result = list(combinations(data, 2))
print(result)
# Output: [(1, 2), (1, 3), (2, 3)]

# Dynamic Programming(DP) Top-down (재귀 + 메모이제이션)
dp = [0] * 100

def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    if dp[n]: return dp[n]
    dp[n] = fib(n - 1) + fib(n - 2)
    return dp[n]

print(fib(10))  # 55
