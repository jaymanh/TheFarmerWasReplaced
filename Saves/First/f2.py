def untillAll():
	Home()
	world = get_world_size()
	while(True):
		harvest()
		if(get_ground_type() != Grounds.Turf):
			till()
		if(get_pos_y() == world - 1):
			move(East)
		move(North)
		if(get_pos_x() == world - 1 and get_pos_y() == world - 1):
			harvest()
			if(get_ground_type() != Grounds.Turf):
				till()
			break
untillAll()