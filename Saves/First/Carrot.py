def FarmCarrot():
	i = 0
	HarvestAll()
	Home()
	world = get_world_size()
	while(i < 1000):
		i += 1
		if(can_harvest()):
			harvest()
			if(get_ground_type() != Grounds.Soil):
				till()
		if(num_items(Items.Carrot_Seed) < 100):
			trade(Items.Carrot_Seed, 100)
		plant(Entities.Carrots)
			
		if(num_items(Items.Water_Tank) < 5):
			trade(Items.Empty_Tank)
		if(get_water() < 0.8):
			use_item(Items.Water_Tank)
		move(North)
		if(get_pos_y() == world -1):
			move(East)