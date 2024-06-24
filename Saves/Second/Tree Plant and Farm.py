def PlantAllTree():
	Home()
	world = get_world_size()
	dir = East
	for i in range(world):
		TreePlantRow(dir)
		if i % 2 == 0:
			dir = West
		else:
			dir = East
		move(North)
		
def TreePlantRow(dir):
	world = get_world_size()
	for i in range(world):
		if get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0 or get_pos_x() % 2 != 0 and get_pos_y() % 2 !=0:
			harvest()
			if get_ground_type() == Grounds.Turf:
				till()
			plant(Entities.Tree)
			TryWater()
		if i != world - 1:
			move(dir)
		
def FarmAllTree():
	Home()
	world = get_world_size()
	dir = East
	for i in range(world):
		TreeFarmRow(dir)
		if i % 2 == 0:
			dir = West
		else:
			dir = East
		move(North)
		
def TreeFarmRow(dir):
	world = get_world_size()
	for i in range(world):
		if (get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0 or get_pos_x() % 2 != 0 and get_pos_y() % 2 !=0) and can_harvest():
			harvest()
			if get_ground_type() == Grounds.Turf:
				till()
			plant(Entities.Tree)
			TryWater()
		if i != world - 1:
			move(dir)
		
		
PlantAllTree()