def DinoAll():
	Home()
	world = get_world_size()
	dir = East
	for i in range(world):
		if not DinoRow(dir):
			return
		if i % 2 == 0:
			dir = West
		else:
			dir = East
		move(North)
	
def DinoRow(dir):
	world = get_world_size()
	for i in range(world):
		if can_harvest():
			harvest()
		if get_ground_type() == Grounds.Soil:
			till()
		if num_items(Items.Egg) < 5:
			if not trade(Items.Egg, 10):
				return False
		use_item(Items.Egg)
		if i != world - 1:
			move(dir)
	return True