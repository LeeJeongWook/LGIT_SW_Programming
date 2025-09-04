
statck = []
'''
append(): 스택의 맨 끝에 요소를 추가합니다.
clear(): 스택의 모든 요소를 제거합니다.
len(): 스택의 길이(요소 개수)를 반환합니다.
pop(): 스택의 맨 끝 요소를 제거하고 반환합니다.
'''

from collections import deque
q = deque()
'''
append(): deque의 오른쪽 끝에 요소를 추가합니다.
appendleft(): deque의 왼쪽 끝에 요소를 추가합니다.
pop(): deque의 오른쪽 끝 요소를 제거하고 반환합니다.
popleft(): deque의 왼쪽 끝 요소를 제거하고 반환합니다.
clear(): deque의 모든 요소를 제거합니다.
index(val): deque에서 특정 값의 첫 번째 인덱스를 반환합니다.
count(val): deque에서 특정 값의 개수를 반환합니다.
'''

# 딕셔너리(dict) : 키(key) → 값(value) 쌍으로 저장
d = {"a": 1, "b": 2}
'''
.keys(): 딕셔너리의 모든 키를 반환합니다.
.values(): 딕셔너리의 모든 값을 반환합니다.
.items(): 딕셔너리의 모든 (키, 값) 쌍을 반환합니다.
.get(key, default=None): 특정 키의 값을 반환하고, 키가 없을 경우 지정된 기본값을 반환합니다.
.pop(key, default=None): 특정 키와 값을 딕셔너리에서 제거하고, 제거된 값을 반환합니다.
.clear(): 딕셔너리의 모든 항목을 제거합니다.
.copy(): 딕셔너리의 얕은 복사본을 반환합니다.
'''
# 집합(set): 값만 저장, 중복 없음, 순서 없음 (중괄호 {} 또는 set() 사용)
s = {1, 2, 3}
b = set() 
'''
.add(element): 집합에 새로운 원소를 추가합니다.
.remove(element): 특정 원소를 제거합니다. 원소가 없으면 KeyError가 발생합니다.
.discard(element): 특정 원소를 제거합니다. 원소가 없어도 에러가 발생하지 않습니다.
.pop(): 임의의 원소 하나를 제거하고 반환합니다. 집합이 비어있으면 KeyError가 발생합니다.
'''
# ===============================================================
# 데이터 입력 받기
def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	ID = list(map(int, readl().split()))
	return N, ID    

# 출력 데이터 포맷 설정
for row in dp:
	print(" ".join(f"{num:>{width}}" for num in row))
	
# 데이터 초기화
arr = [0 for _ in range(5)]
table = [[0] * 5 for _ in range(5)]
visited = [[0 for _ in range(m)] for _ in range(n)]

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
min_heap, max_heap = []

# 요소 추가
heapq.heappush(min_heap, 4)
# 최소값 제거
min_value = heapq.heappop(min_heap)

# 요소 추가 (값에 음수를 취해 추가)
heapq.heappush(max_heap, -4)
# 최대값 제거
max_value = -heapq.heappop(max_heap)

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
