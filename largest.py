def maximum(a,b,c):
	if(a>=b) and (a>=c):
		largest=a
	elif(b>=a) and (b>=c):
		largest=b
	else:
		largest=c
	return largest
a=10
b=42
c=65
print(maximum(a,b,c))