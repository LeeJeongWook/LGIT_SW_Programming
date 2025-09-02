def solution(n, times):
    # ���� Ž���� Ž�� ���� ����
    start = 1  # �ּ� �ð��� 1�к��� ����
    end = max(times) * n # �ִ� �ð�: ���� ���� �ɸ��� �ɻ���� ��� ����� ó���ϴ� ���
    answer = end # �ּ� �ð��� ������ ����, �ʱⰪ�� �ִ� �ð����� ����

    while start <= end:
        mid = (start + end) // 2
        
        # mid �ð� ���� ó���� �� �ִ� �� ��� �� ���
        total_people = 0
        for time in times:
            total_people += mid // time

        if total_people >= n:
            # mid �ð� ���� ��� ����� ó���� �� �ִ� ���
            # �� ª�� �ð����ε� �������� Ž���ϱ� ���� end�� ����
            answer = mid
            end = mid - 1
        else:
            # mid �ð� ���� ��� ����� ó���� �� ���� ���
            # �ð��� �� �÷��� �ϹǷ� start�� �ø�
            start = mid + 1
            
    return answer