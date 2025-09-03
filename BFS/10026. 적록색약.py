from collections import deque

# �Է� ó��
N = int(input())
picture = [list(input()) for _ in range(N)]

# �����¿� �̵� ��ǥ
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# BFS �Լ� ����
def bfs(x, y, color, picture, visited):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]

            # ���� ���� �ְ�, ���� �湮 �� ������ ���� ���� ���
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and picture[nx][ny] == color:
                visited[nx][ny] = True
                queue.append((nx, ny))

# ���� ��� �Լ�
def count_regions(picture, is_colorblind):
    visited = [[False] * N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            # �湮���� ���� ���ο� ���� �߰�
            if not visited[i][j]:
                count += 1
                color = picture[i][j]

                # ���ϻ����� ��� R�� G�� ������ ������ ó��
                if is_colorblind and color in ('R', 'G'):
                    bfs(i, j, 'C', [['C' if ch in ('R', 'G') else ch for ch in row] for row in picture], visited)
                else:
                    bfs(i, j, color, picture, visited)
    
    return count

# ���ϻ����� �ƴ� ����� ���� ���� ���
normal_count = count_regions(picture, False)

# ���ϻ����� ����� ���� ���� ���
colorblind_count = count_regions(picture, True)

# ��� ���
print(normal_count, colorblind_count)