dr = ( -1, 1, 0, 0, -1, -1, 1, 1)
dc = ( 0, 0, -1, 1, 1, -1, -1, 1)

def Touch(r, c):

	if A[r][c] == 0: V = 1
	else: V = 0
	A[r][c] = V

	for k in range(8):
		nr = r
		nc = c
		flag = 0
		bomb = False
		
		while True:
			nr = nr + dr[k]
			nc = nc + dc[k]
			if nr < 0 or nr >= H or nc < 0 or nc >= W:
				break
			
			if A[nr][nc] == 2:
				bomb = True
			if A[nr][nc] == V:
				flag = 1
				break
				
		if flag == 1:
			nr = r
			nc = c

			if bomb:
				while True:
					if nr < 0 or nr >= H or nc < 0 or nc >= W:
						break
					A[nr][nc] = V
					nr = nr + dr[k]
					nc = nc + dc[k]
			else:
				while True:
					nr = nr + dr[k]
					nc = nc + dc[k]
					if A[nr][nc] == V:
						break

					A[nr][nc] = V




























