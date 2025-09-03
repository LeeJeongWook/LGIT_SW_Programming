from collections import deque

def solve():
    l = int(input())
    start_x, start_y = map(int, input().split())
    target_x, target_y = map(int, input().split())

    # �������� ��ǥ���� ������ 0�� �̵�
    if start_x == target_x and start_y == target_y:
        print(0)
        return

    # ����Ʈ�� �̵��� �� �ִ� 8���� ����
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]

    queue = deque([(start_x, start_y, 0)])
    visited = [[False] * l for _ in range(l)]
    visited[start_x][start_y] = True

    while queue:
        x, y, moves = queue.popleft()

        # 8���� �������� �̵��ϸ� Ž��
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            # ���� ��ġ�� ü���� ���� �ȿ� �ִ��� Ȯ��
            if 0 <= nx < l and 0 <= ny < l:
                # ���� ��ġ�� ���� �湮���� �ʾҴٸ�
                if not visited[nx][ny]:
                    # ��ǥ ��ġ�� ���������� �̵� Ƚ�� ���
                    if nx == target_x and ny == target_y:
                        print(moves + 1)
                        return
                    
                    # ť�� ���� ��ġ�� �̵� Ƚ���� �߰��ϰ� �湮 ó��
                    visited[nx][ny] = True
                    queue.append((nx, ny, moves + 1))


def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()