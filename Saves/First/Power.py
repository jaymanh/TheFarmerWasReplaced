def FarmPower():
	i = 0
	HarvestAll()
	Home()
	world = get_world_size()
	maxsunflower = 0
	j = False
	while(i < 1000):
		i += 1
		
		plant(Entities.Sunflower)
		if(j == False):
			if(get_entity_type() == Entities.Sunflower) and measure() > maxsunflower:
				maxsunflower = measure()
			else:
				plant(Entities.Sunflower)
			if(get_ground_type() != Grounds.Soil):
				till()
			if num_items(Items.Sunflower_Seed) < 100:
				if not BuySeeds(Items.Sunflower_Seed):
					break
			
		else:
			if(get_entity_type() == Entities.Sunflower) and measure() == maxsunflower:
				harvest()
				maxsunflower = 0
				plant(Entities.Sunflower)
		
		
		if(num_items(Items.Water_Tank) < 5):
			trade(Items.Empty_Tank)
		if(get_water() < 0.8):
			use_item(Items.Water_Tank)
		if(get_pos_x() == 0 and get_pos_y() == 0 and j):
			j = False
		elif(get_pos_x() == 0 and get_pos_y() == 0 and j == False):
			j = True
		move(North)
		if(get_pos_y() == world -1):
			move(East)