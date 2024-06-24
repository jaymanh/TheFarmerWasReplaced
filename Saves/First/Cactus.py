def FarmCactus():
	i = 0
	HarvestAll()
	Home()
	world = get_world_size()
	j = True
	while(i < 10):
		Do_Cactus()
		i += 1