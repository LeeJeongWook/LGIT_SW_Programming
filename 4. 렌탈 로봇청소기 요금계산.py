# 수정전 로봇청소기 1회 사용 시작시간과 종료시간을 이용하여 요금을 계산한 코드

def InputData():
	s = input()
	e = input()
	return s, e

def ComputeTime():
	global stime
	global etime
	s = int(stime[0:2]) * 60 + int(stime[3:])
	e = int(etime[0:2]) * 60 + int(etime[3:])
	if s > e:
		e += 24 * 60
	return (e - s)

def Solve():
	t = ComputeTime()
	if t < 30 : return 500
	p = 500 + ((t - 30) // 10 + 1) * 300
	if t % 10 == 0:
		p -= 300
	if p > 30000:
		p = 30000
	return p

def OutputData(sol):
	print(sol)

stime, etime = InputData() #입력 
sol = Solve() # 문제 해결
OutputData(sol) # 출력
