def PlantAll(Crop = Entities.Grass, Seed = Items.Carrot_Seed):
	Home()
	if Crop == Entities.Tree:
		PlantAllTree()
		return
	world = get_world_size()
	dir = East
	for i in range(world):
		if not PlantRow(dir, Crop, Seed):
			return
		if i % 2 == 0:
			dir = West
		else:
			dir = East
		move(North)

def PlantRow(dir, Crop, Seed):
	world = get_world_size()
	for i in range(world):
		harvest()
		if get_ground_type() == Grounds.Turf:
			till()
		if num_items(Seed) < 5 and not (Crop == Entities.Bush or Crop == Entities.Grass):
			if not trade(Seed, 10):
				return False
		plant(Crop)
		TryWater()
		if i != world - 1:
			move(dir)
	return True
PlantAll(Entities.Bush)