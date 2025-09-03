from collections import deque

def solve():
    m, n, k = map(int, input().split())

    # 모눈종이 배열 초기화 (0: 빈 공간, 1: 직사각형)
    board = [[0] * n for _ in range(m)]

    # 직사각형 영역을 1로 표시
    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        for y in range(y1, y2):
            for x in range(x1, x2):
                board[y][x] = 1

    # 방문 여부 배열
    visited = [[False] * n for _ in range(m)]
    
    # 4가지 방향 (상, 하, 좌, 우)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    area_counts = []
    
    # 전체 모눈종이를 탐색
    for i in range(m):
        for j in range(n):
            # 아직 방문하지 않은 빈 공간을 찾으면 BFS 시작
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

                        # 모눈종이 범위 내에 있고, 빈 공간이며, 방문하지 않았다면
                        if 0 <= nx < n and 0 <= ny < m and board[ny][nx] == 0 and not visited[ny][nx]:
                            visited[ny][nx] = True
                            queue.append((nx, ny))
                            area_size += 1
                
                area_counts.append(area_size)

    # 영역의 개수와 넓이를 정렬하여 출력
    print(len(area_counts))
    area_counts.sort()
    print(*area_counts)

solve()