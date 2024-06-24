def Home():
	for i in range(get_pos_x()):
		move(West)
	for i in range(get_pos_y()):
		move(South)
		
def GoTo(x = 0, y = 0):
	cx = get_pos_x()
	cy = get_pos_y()
	if(cx == x):
		pass
	elif(cx > x):
		mx = cx - x
		for i in range(mx):
			move(West)
	else:
		mx = x - cx
		for i in range(mx):
			move(East)
	if(cy == y):
		pass
	elif(cy > y):
		my = cy - y
		for i in range(my):
			move(South)
	else:
		my = y - cy
		for i in range(my):
			move(North)
Home()