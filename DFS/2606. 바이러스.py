def dfs(graph, visited, node):
    visited[node] = True
    count = 1  # 현재 노드도 감염됨
    for neighbor in graph[node]:
        if not visited[neighbor]:
            count += dfs(graph, visited, neighbor)
    return count

# 입력
n = int(input())  # 컴퓨터 수
m = int(input())  # 연결 수

# 그래프 초기화
graph = [[] for _ in range(n + 1)]

# 연결 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 여부 초기화
visited = [False] * (n + 1)

# 1번 컴퓨터부터 시작 (자기 자신 제외)
infected_count = dfs(graph, visited, 1) - 1

print(infected_count)
