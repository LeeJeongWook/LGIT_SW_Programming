# ===============================================================
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

# ===============================================================
# 정렬
nums = [5, 2, 9, 1]
sorted_nums = sorted(nums)
# Output: [1, 2, 5, 9]
print(sorted(nums, reverse=True))
# Output: [9, 5, 2, 1]

# Lamda Ex
words = ['banana', 'apple', 'cherry', 'kiwi']
# sort(): List의 메서드, 원본 리스트 변경
words.sort(key=lambda x: len(x))
# sorted(): 모든 반복 가능한 객체(튜플, 딕셔너리 등)에서 사용 가능, 정렬된 새로운 리스트를 반환, 원본 변경 x
sorted_words = sorted(words, key=lambda x: len(x))
# Output: ['kiwi', 'apple', 'banana', 'cherry']

prior = {"R":2, "G":1, "B":0}
data = []
for col in ["R", "G", "B"]:
	data.append((area[col], grid[col], col))
data.sort(key=lambda x : (-x[0], -x[1], -prior[x[2]]))

# ===============================================================
# DFS
def dfs(graph, v, visited):
    visited[v] = True
    
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
        
        for next in graph[v]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True

# ===============================================================
# 순열: 순서 고려 o
from itertools import permutations

data = [1, 2, 3]
result = list(permutations(data, 2))
print(result)
# Output: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# 조합: 순서 고려 x
from itertools import combinations

data = [1, 2, 3]
result = list(combinations(data, 2))
print(result)
# Output: [(1, 2), (1, 3), (2, 3)]

# 데카르트 곱: 모든 가능한 조합, 중복 선택 o
from itertools import product

data = ['A', 'B']
product_result = product(data, repeat=2)
print(list(product_result))
# 출력: [('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')]

# ===============================================================
# 최소힙: 가장 작은 값이 항상 루트 노드에 위치
import heapq

# 빈 리스트로 힙 초기화
min_heap = []

# 요소 추가 (자동으로 최소 힙 정렬 유지)
heapq.heappush(min_heap, 4)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 7)
heapq.heappush(min_heap, 2)
print(f"최소 힙: {min_heap}") # 출력: 최소 힙: [1, 2, 7, 4]

# 최소값 제거 (가장 작은 값인 1이 반환되고 제거됨)
min_value = heapq.heappop(min_heap)
print(f"제거된 최소값: {min_value}") # 출력: 제거된 최소값: 1
print(f"최소값 제거 후 힙: {min_heap}") # 출력: 최소값 제거 후 힙: [2, 4, 7]


# 최대힙: 가장 큰 값이 항상 루트 노드에 위치
import heapq

# 빈 리스트로 최대 힙 초기화
max_heap = []

# 요소 추가 (값에 음수를 취해 추가)
heapq.heappush(max_heap, -4)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -7)
heapq.heappush(max_heap, -2)
print(f"내부적으로 음수로 저장된 힙: {max_heap}") # 출력: 내부적으로 음수로 저장된 힙: [-7, -4, -2, -1]

# 최대값 제거 (가장 작은 음수(-7)가 반환되고, 다시 양수(7)로 변환)
max_value = -heapq.heappop(max_heap)
print(f"제거된 최대값: {max_value}") # 출력: 제거된 최대값: 7
print(f"최대값 제거 후 힙: {max_heap}") # 출력: 최대값 제거 후 힙: [-4, -2, -1]
# ===============================================================