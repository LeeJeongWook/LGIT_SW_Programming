def solution(triangle):
    # dp ���̺��� �ﰢ���� ������ ũ��� �ʱ�ȭ (���� ����)
    dp = [row[:] for row in triangle]

    # �� ��° �ٺ��� ������ �ٱ��� ���������� ���
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            # �� ���� ĭ
            if j == 0:
                dp[i][j] += dp[i-1][j]
            # �� ������ ĭ
            elif j == i:
                dp[i][j] += dp[i-1][j-1]
            # �߰� ĭ
            else:
                dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

    # ������ �ٿ��� �ִ� ��ȯ
    return max(dp[-1])