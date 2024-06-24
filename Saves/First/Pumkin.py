def FarmPumkin():
	i = 0
	HarvestAll()
	Home()
	world = get_world_size() -1
	emptySpace = False
	
	while(i < 1000):
		i += 1
		#print(plist[1][1])
		if(get_ground_type() != Grounds.Soil):
				till()
		if num_items(Items.Pumpkin_Seed) < 100:
			if not BuySeeds(Items.Pumpkin_Seed):
				NewCarrot({Items.Carrot: 10000})
				return
		plant(Entities.Pumpkin)
		
		if(get_pos_x() == 0 and get_pos_y() == 0):
			emptySpace = False
		if(get_entity_type() != Entities.Pumpkin):
			emptySpace = True
		if(get_pos_x() == world and get_pos_y() == world and emptySpace == False):
			harvest()
		
		if(num_items(Items.Water_Tank) < 5):
			trade(Items.Empty_Tank)
		if(get_water() < 0.8):
			use_item(Items.Water_Tank)
		move(North)
		if(get_pos_y() == world -1):
			move(East)
FarmPumkin()