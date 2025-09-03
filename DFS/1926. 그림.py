# 입력 처리
n, m = map(int, input().split())

# 도화지 정보 입력
picture = []
for _ in range(n):
    picture.append(list(map(int, input().split())))

# 방문 여부 초기화
visited = [[0 for _ in range(m)] for _ in range(n)]

# 방향 벡터 (상, 하, 좌, 우)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# DFS 함수 정의
def dfs(x, y):
    stack = [(x, y)]
    visited[y][x] = 1
    area_size = 0

    while stack:
        cx, cy = stack.pop()
        area_size += 1

        for i in range(4):  # 상, 하, 좌, 우 탐색
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < m and 0 <= ny < n and picture[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = 1
                stack.append((nx, ny))

    return area_size

# 그림 개수와 최대 넓이 계산
pic_count = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if picture[i][j] == 1 and not visited[i][j]:
            pic_count += 1  # 새로운 그림 발견
            max_area = max(max_area, dfs(j, i))  # 넓이 계산 후 최댓값 갱신

# 출력
print(pic_count)
print(max_area)