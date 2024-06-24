def FarmAll(Crop = Entities.Grass, Seed = Items.Carrot_Seed):
	Home()
	if Crop == Entities.Tree:
		FarmAllTree()
		return
	world = get_world_size()
	dir = East
	for i in range(world):
		if not FarmRow(dir, Crop, Seed):
			return
		if i % 2 == 0:
			dir = West
		else:
			dir = East
		move(North)
	
def FarmRow(dir, Crop, Seed):
	world = get_world_size()
	for i in range(world):
		if can_harvest():
			harvest()
			if get_ground_type() == Grounds.Turf:
				till()
			if num_items(Seed) < 5 and not (Crop == Entities.Grass or Crop == Entities.Bush):
				if not trade(Seed, 10):
					return False
			plant(Crop)
			TryWater()
		if i != world - 1:
			move(dir)
	return True