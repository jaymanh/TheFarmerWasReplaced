def HarvestAll():
	Home()
	dir = East
	for i in range(get_world_size()):
		if i % 2 == 0:
			dir = East
		else:
			dir = West
		HarvestRow(dir)
		move(North)
	
	
def HarvestRow(dir):
	world = get_world_size()
	for i in range(world):
		harvest()
		if i != world - 1:
			move(dir)
HarvestAll()