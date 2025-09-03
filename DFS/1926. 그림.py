# �Է� ó��
n, m = map(int, input().split())

# ��ȭ�� ���� �Է�
picture = []
for _ in range(n):
    picture.append(list(map(int, input().split())))

# �湮 ���� �ʱ�ȭ
visited = [[0 for _ in range(m)] for _ in range(n)]

# ���� ���� (��, ��, ��, ��)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# DFS �Լ� ����
def dfs(x, y):
    stack = [(x, y)]
    visited[y][x] = 1
    area_size = 0

    while stack:
        cx, cy = stack.pop()
        area_size += 1

        for i in range(4):  # ��, ��, ��, �� Ž��
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < m and 0 <= ny < n and picture[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = 1
                stack.append((nx, ny))

    return area_size

# �׸� ������ �ִ� ���� ���
pic_count = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if picture[i][j] == 1 and not visited[i][j]:
            pic_count += 1  # ���ο� �׸� �߰�
            max_area = max(max_area, dfs(j, i))  # ���� ��� �� �ִ� ����

# ���
print(pic_count)
print(max_area)