def solution(m, n, puddles):
    # m�� n�� ������ ���� 2���� ����Ʈ�� ����
    dp = [[0] * m for _ in range(n)]

    # 1. �������� ��ġ�� �̸� ǥ��
    # ������ ��ǥ�� (1,1)�� ����Ʈ �ε��� (0,0)�� ����
    for x, y in puddles:
        dp[y - 1][x - 1] = -1  # �������� ǥ��

    # 2. DP ���̺� ä���
    for i in range(n):
        for j in range(m):
            # �������̴� �ǳʶٱ�
            if dp[i][j] == -1:
                dp[i][j] = 0  # ��ΰ� 0��
                continue
            
            # ������
            if i == 0 and j == 0:
                dp[i][j] = 1
                continue

            # ���ʰ� ���� ��θ� ���Ͽ� ���� ��ġ�� ��� ���� ���
            up = dp[i - 1][j] if i > 0 else 0
            left = dp[i][j - 1] if j > 0 else 0

            dp[i][j] = (up + left) % 1000000007

    # 3. �б� ��ġ�� �ִ� ��� ���� ��ȯ
    return dp[n - 1][m - 1]