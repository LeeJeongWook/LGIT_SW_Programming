def solution(n, results):
    # 1. �׷��� �ʱ�ȭ
    # ���� ���踦 ������ 2���� �迭 (n+1 x n+1)
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    
    # �������� ���� ���踦 �׷����� �ݿ�
    for winner, loser in results:
        graph[winner][loser] = True
        
    # 2. �÷��̵�-���� �˰��� ����
    # k: ���� ���, i: ���� ���, j: ���� ���
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                # i�� k�� �̱�� k�� j�� �̰�ٸ�, i�� j�� �̱��
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = True
                    
    # 3. ���� Ȯ�� ���� �� ���
    answer = 0
    for i in range(1, n + 1):
        win_count = 0
        lose_count = 0
        # i�� �̱� ���� �� ����
        for j in range(1, n + 1):
            if graph[i][j]:
                win_count += 1
        # i���� �� ���� �� ���� (j�� i�� �̰���� Ȯ��)
        for j in range(1, n + 1):
            if graph[j][i]:
                lose_count += 1
        
        # ������ Ȯ���� �������� Ȯ�� (�̱� ���� + �� ���� = n - 1)
        if win_count + lose_count == n - 1:
            answer += 1
            
    return answer