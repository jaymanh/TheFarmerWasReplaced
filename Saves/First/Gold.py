def FarmGold():
	i = 0
	HarvestAll()
	Home()
	world = get_world_size()
	while(i < 10):
		i += 1
		Maze()