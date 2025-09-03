from collections import deque

# 입력 처리
N = int(input())
picture = [list(input()) for _ in range(N)]

# 상하좌우 이동 좌표
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# BFS 함수 정의
def bfs(x, y, color, picture, visited):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]

            # 범위 내에 있고, 아직 방문 안 했으며 같은 색일 경우
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and picture[nx][ny] == color:
                visited[nx][ny] = True
                queue.append((nx, ny))

# 구역 계산 함수
def count_regions(picture, is_colorblind):
    visited = [[False] * N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            # 방문하지 않은 새로운 구역 발견
            if not visited[i][j]:
                count += 1
                color = picture[i][j]

                # 적록색약인 경우 R과 G를 동일한 색으로 처리
                if is_colorblind and color in ('R', 'G'):
                    bfs(i, j, 'C', [['C' if ch in ('R', 'G') else ch for ch in row] for row in picture], visited)
                else:
                    bfs(i, j, color, picture, visited)
    
    return count

# 적록색약이 아닌 사람의 구역 개수 계산
normal_count = count_regions(picture, False)

# 적록색약인 사람의 구역 개수 계산
colorblind_count = count_regions(picture, True)

# 결과 출력
print(normal_count, colorblind_count)