serie = 0.0
x = 1.0
a = 0

while x <= 15:
	if x % 2 == 0:
		serie = serie-(x/(x*x))
		print "par", x, serie
	else:
		serie = serie+(x/(x*x))
		print "impar",x, serie
	x = x+1
print serie
