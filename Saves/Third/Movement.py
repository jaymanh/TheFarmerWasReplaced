def Home():
	while get_pos_x() != 0:
		move(West)
	while get_pos_y() != 0:
		move(South)

def GoTo(x, y):
	while get_pos_x() != x:
		if get_pos_x() < x:
			move(East)
		else:
			move(West)
	while get_pos_y() != y:
		if get_pos_y() < y:
			move(North)
		else:
			move(South)

def Next():
	world = get_world_size() -1
	endx = world
	endy = world
	if world % 2 != 0:
		endx = 0
	x = get_pos_x()
	y = get_pos_y()
	dir = East
	if endx == x and endy == y:
		move(North)
		dir = East
		if y % 2 != 0:
			return
	elif x == world and y % 2 == 0:
		dir = North
	elif x != world and y % 2 ==0:
		dir = East
	elif x != 0 and y % 2 != 0:
		dir = West
	elif x == 0 and y % 2 != 0:
		dir = North
	move(dir)