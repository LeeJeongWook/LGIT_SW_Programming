from collections import deque

def solution(n, vertex):
    # 1. 그래프를 인접 리스트로 표현
    graph = [[] for _ in range(n + 1)]
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)

    # 2. BFS를 위한 거리 배열 및 큐 초기화
    distances = [-1] * (n + 1)
    queue = deque([1])
    distances[1] = 0

    # 3. BFS 탐색
    while queue:
        current_node = queue.popleft()
        
        for neighbor in graph[current_node]:
            if distances[neighbor] == -1: # 아직 방문하지 않은 노드라면
                distances[neighbor] = distances[current_node] + 1
                queue.append(neighbor)

    # 4. 가장 먼 노드까지의 거리와 개수 계산
    max_distance = max(distances)
    
    answer = 0
    for distance in distances:
        if distance == max_distance:
            answer += 1
            
    return answer