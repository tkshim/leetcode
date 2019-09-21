

x = [5,2,4,3,1]
x.sort()

y=4

def bs(x,y):
	z=len(x)/2
	print x[z]
	if y == x[z]:
		print "bingo"
	elif y < x[z]:
		print "no"
	else:
		bs(x[z],y)
		print "boo"
print bs(x,y)
