def Home():
	world = get_world_size() -1
	if get_pos_x() == 0:
		pass
	elif get_pos_x() <= (world / 2):
		while get_pos_x() != 0:
			move(West)
	else:
		while get_pos_x() !=0:
			move(East)

	if get_pos_y() == 0:
		pass
	elif get_pos_y() <= (world / 2):
		while get_pos_y() != 0:
			move(South)
	else:
		while get_pos_y() !=0:
			move(North)

def GoTo(x, y):
	cx = get_pos_x()
	cy = get_pos_y()
	
	if cx == x:
		pass
	elif cx > x:
		dx = cx - x
		for i in range(dx):
			move(West)
	else:
		dx = x - cx
		for i in range(dx):
			move(East)
	if cy == y:
		pass
	elif cy > y:
		dy = cy - y
		for i in range(dy):
			move(South)
	else:
		dy = y - cy
		for i in range(dy):
			move(North)
	
Home()