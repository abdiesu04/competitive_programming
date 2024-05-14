# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

for t in range(int(input())):
	a=int(input())
	b=a&-a
	while (a==b or (a&b)==0):
		b+=1
	print(b)