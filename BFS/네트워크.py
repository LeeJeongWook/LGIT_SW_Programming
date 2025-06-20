from collections import deque

def solution(n, computers):
    answer = 0
    
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            bfs(n, computers, com, visited)
            answer += 1
    return answer

def bfs(n, computers, com, visited):
    visited[com] = True
    q = deque()
    q.append(com)
    
    while q:
        com = q.pop()
        visited[com] = True
        for connect in range(n):
            if connect != com and computers[com][connect] == True:
                if visited[connect] == False:
                    q.append(connect)
