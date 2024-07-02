def MesureAll():
	a = measure()
	b = measure(North)
	c = measure(East)
	d = measure(South)
	e = measure(West)
	return [a, b, c, d, e]
print(MesureAll())