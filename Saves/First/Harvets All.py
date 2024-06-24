def HarvestAll():
	if(num_unlocked(Unlocks.Senses)):
		world = get_world_size()
		Home()
		while(True):
			harvest()
			if(get_pos_y() == world - 1):
				move(East)
			move(North)
			if(get_pos_x() == world - 1 and get_pos_y() == world - 1):
				harvest()
				return
	return
HarvestAll()
		