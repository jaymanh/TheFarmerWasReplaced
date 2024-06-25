def Home():
	half_world_size = get_world_size() / 2
	dirx = East
	diry = North
	
	if get_pos_x() < half_world_size:
		dir = West
	else:
		dir = East
	if get_pos_y() < half_world_size:
		dir = South
	else:
		dir = North

	while get_pos_x() != 0:
		move(dirx)
	while get_pos_y() != 0:
		move(diry)
		
def basicGoTo(x, y):
	while x != get_pos_x():
		if x > get_pos_x():
			move(East)
		else:
			move(West)
	while y != get_pos_y():
		if y < get_pos_y():
			move(South)
		else:
			move(North)

def GoTo(x, y):
	distance_x = x - get_pos_x()
	distance_y = y - get_pos_y()

	if distance_x:
		if distance_x >=0:
			if distance_x <= get_world_size() //2:
				for i in range(distance_x):
					move(East)
			else:
				for i in range(get_world_size() - distance_x):
					move(West)
		else:
			if -distance_x <= get_world_size() //2:
				for i in range(-distance_x):
					move(West)
			else:
				for i in range(get_world_size() + distance_x):
					move(East)

	if distance_y:
		if distance_y >=0:
			if distance_y <= get_world_size() //2:
				for i in range(distance_y):
					move(North)
			else:
				for i in range(get_world_size() - distance_y):
					move(South)
		else:
			if -distance_y <= get_world_size() //2:
				for i in range(-distance_y):
					move(South)
			else:
				for i in range(get_world_size() + distance_y):
					move(North)
			

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