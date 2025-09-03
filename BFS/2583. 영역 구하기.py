from collections import deque

def solve():
    m, n, k = map(int, input().split())

    # ������ �迭 �ʱ�ȭ (0: �� ����, 1: ���簢��)
    board = [[0] * n for _ in range(m)]

    # ���簢�� ������ 1�� ǥ��
    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        for y in range(y1, y2):
            for x in range(x1, x2):
                board[y][x] = 1

    # �湮 ���� �迭
    visited = [[False] * n for _ in range(m)]
    
    # 4���� ���� (��, ��, ��, ��)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    area_counts = []
    
    # ��ü �����̸� Ž��
    for i in range(m):
        for j in range(n):
            # ���� �湮���� ���� �� ������ ã���� BFS ����
            if board[i][j] == 0 and not visited[i][j]:
                area_size = 0
                queue = deque([(j, i)]) # (x, y)
                visited[i][j] = True
                area_size += 1

                while queue:
                    x, y = queue.popleft()
                    
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        # ������ ���� ���� �ְ�, �� �����̸�, �湮���� �ʾҴٸ�
                        if 0 <= nx < n and 0 <= ny < m and board[ny][nx] == 0 and not visited[ny][nx]:
                            visited[ny][nx] = True
                            queue.append((nx, ny))
                            area_size += 1
                
                area_counts.append(area_size)

    # ������ ������ ���̸� �����Ͽ� ���
    print(len(area_counts))
    area_counts.sort()
    print(*area_counts)

solve()