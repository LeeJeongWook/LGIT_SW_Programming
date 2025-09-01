def solution(begin, target, words):
    answer = 0
    visited = [0 for _ in range(len(words))]
    if target in words:
        return dfs(begin, target, words, visited, 0)
    else:
        return 0

def Check(a, b):
    cnt = 0
    for i in range(len(a)):
        if(a[i] != b[i]):
            cnt += 1
    if cnt == 1:
        return True
    return False

def dfs(word, target, words, visited, cnt):
    if word == target:
        return cnt
    min_cnt = float('inf')
    for i in range(len(words)):
        if not visited[i] and Check(word, words[i]):
            visited[i] = True
            result = dfs(words[i], target, words, visited, cnt + 1)
            if result < min_cnt:
                min_cnt = result
            visited[i] = False
    return min_cnt