from collections import deque

def solve():
    l = int(input())
    start_x, start_y = map(int, input().split())
    target_x, target_y = map(int, input().split())

    # 시작점과 목표점이 같으면 0번 이동
    if start_x == target_x and start_y == target_y:
        print(0)
        return

    # 나이트가 이동할 수 있는 8가지 방향
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]

    queue = deque([(start_x, start_y, 0)])
    visited = [[False] * l for _ in range(l)]
    visited[start_x][start_y] = True

    while queue:
        x, y, moves = queue.popleft()

        # 8가지 방향으로 이동하며 탐색
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            # 다음 위치가 체스판 범위 안에 있는지 확인
            if 0 <= nx < l and 0 <= ny < l:
                # 다음 위치를 아직 방문하지 않았다면
                if not visited[nx][ny]:
                    # 목표 위치에 도달했으면 이동 횟수 출력
                    if nx == target_x and ny == target_y:
                        print(moves + 1)
                        return
                    
                    # 큐에 다음 위치와 이동 횟수를 추가하고 방문 처리
                    visited[nx][ny] = True
                    queue.append((nx, ny, moves + 1))


def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()