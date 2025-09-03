def dfs(graph, visited, node):
    visited[node] = True
    count = 1  # ���� ��嵵 ������
    for neighbor in graph[node]:
        if not visited[neighbor]:
            count += dfs(graph, visited, neighbor)
    return count

# �Է�
n = int(input())  # ��ǻ�� ��
m = int(input())  # ���� ��

# �׷��� �ʱ�ȭ
graph = [[] for _ in range(n + 1)]

# ���� ���� �Է�
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# �湮 ���� �ʱ�ȭ
visited = [False] * (n + 1)

# 1�� ��ǻ�ͺ��� ���� (�ڱ� �ڽ� ����)
infected_count = dfs(graph, visited, 1) - 1

print(infected_count)
