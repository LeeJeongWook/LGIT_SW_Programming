from collections import deque

def solution(n, vertex):
    # 1. �׷����� ���� ����Ʈ�� ǥ��
    graph = [[] for _ in range(n + 1)]
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)

    # 2. BFS�� ���� �Ÿ� �迭 �� ť �ʱ�ȭ
    distances = [-1] * (n + 1)
    queue = deque([1])
    distances[1] = 0

    # 3. BFS Ž��
    while queue:
        current_node = queue.popleft()
        
        for neighbor in graph[current_node]:
            if distances[neighbor] == -1: # ���� �湮���� ���� �����
                distances[neighbor] = distances[current_node] + 1
                queue.append(neighbor)

    # 4. ���� �� �������� �Ÿ��� ���� ���
    max_distance = max(distances)
    
    answer = 0
    for distance in distances:
        if distance == max_distance:
            answer += 1
            
    return answer