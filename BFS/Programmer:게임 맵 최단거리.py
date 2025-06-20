from collections import deque

def solution(maps):
    answer = 0
    m = len(maps)
    n = len(maps[0])
    
    q = deque()
    q.append([0,0])
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or m <= nr or nc < 0 or n <= nc: continue
            elif maps[nr][nc] == 1:
                maps[nr][nc] += maps[r][c] 
                q.append([nr, nc])
                
    return -1 if maps[m-1][n-1] < 2 else maps[m-1][n-1]
