def FarmWood():
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
				
		if(get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0):
			plant(Entities.Tree)
		elif(get_pos_x() % 2 != 0 and get_pos_y() % 2 !=0):
			plant(Entities.Tree)
		else:
			plant(Entities.Grass)
			
		if(num_items(Items.Water_Tank) < 5):
			trade(Items.Empty_Tank)
		if(get_water() < 0.8):
			use_item(Items.Water_Tank)
		move(North)
		if(get_pos_y() == world -1):
			move(East)