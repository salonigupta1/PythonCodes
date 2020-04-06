#Code to find maximum energy
def dist (n,k,d,m,a):
	s=[]
	t = a
	d1=d
	count=0
	while(count < len(t)):
		x = t.pop()
		if x>=t[-1]:
			val = x*m
			s.append(val)
			# print(s)
			d1-=1
			if d1==0:
				s.append(0)
				# print("d1",s)
				count+=1
				t.pop()
			else:
				if len(t)>1:
					if t[-1]>t[-2]:
						x = t.pop()
						val = x*m
						s.append(val)
						# print("t1",s)
						d1-=1
						t.pop()
					else:
						t.pop()
						s.append(0)
						# print("else",s)
						count+=1
				else:
					break
	if count==k:
		s.append(t[0])
		# print(s)
	else:
		s.append(0)

	# print(n,k,d,m,a)
	return sum(s)
	
if __name__=="__main__":
	t = int(input())
	for _ in range(t):
		n,k,d,m = map(int,input().split())
		a = list(map(int,input().split()))
		# print(n,k,d,m,a)
		res = dist(n,k,d,m,a)
		print(res)
