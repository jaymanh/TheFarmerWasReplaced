maxsunflower = 0
HarvestAll()
harvest()
world = get_world_size() -1
j = False
Home()
while(True):
	if(get_pos_x() == 0):
		if(get_pos_y() == 2 or get_pos_y() == 3 or get_pos_y() == 4 or get_pos_y() == 5 or get_pos_y() == 8 or get_pos_y() == 9):
			if(can_harvest() and get_pos_y() == 3 or get_pos_y() == 4 or get_pos_y() == 8):
				harvest()
			if(num_items(Items.Pumpkin_Seed) < 10):
				trade(Items.Pumpkin_Seed, 10)
			if(get_ground_type() != Grounds.Soil):
				till()
			plant(Entities.Pumpkin)
		
		elif(get_pos_y() == 0 or get_pos_y() == 1 or get_pos_y() >= 5):
			if(can_harvest()):
				harvest()
			if(get_ground_type() != Grounds.Soil):
				till()
			if(num_items(Items.Carrot_Seed) < 10):
				trade(Items.Carrot_Seed, 100)
			plant(Entities.Carrots)
		else:
			if(can_harvest()):
				harvest()
			if(num_items(Items.Cactus_Seed) < 10):
				trade(Items.Cactus_Seed, 10)
			plant(Entities.Cactus)
			
		
	elif(get_pos_x() == 1):
		if(get_pos_y() == 2 or get_pos_y() == 3 or get_pos_y() == 4 or get_pos_y() == 5 or get_pos_y() == 8 or get_pos_y() == 9):
			if(num_items(Items.Pumpkin_Seed) < 10):
				trade(Items.Pumpkin_Seed, 10)
			if(get_ground_type() != Grounds.Soil):
				till()
			plant(Entities.Pumpkin)
			
		elif(get_pos_y() == 0 or get_pos_y() == 1 or get_pos_y() >= 5):
			if(can_harvest()):
				harvest()
			if(get_ground_type() != Grounds.Soil):
				till()		
			plant(Entities.Carrots)
		
	elif(get_pos_x() == 2):
		if(can_harvest()):
			harvest()
		if(get_ground_type() != Grounds.Soil):
			till()
		if(get_pos_y() > 4 or get_pos_y() == 1 or get_pos_y() == 3):
			plant(Entities.Grass)
		else:
			plant(Entities.Tree)
			
	elif(get_pos_x() >= 4):
		plant(Entities.Sunflower)
		if(j == False):
			if(get_entity_type() == Entities.Sunflower) and measure() > maxsunflower:
				maxsunflower = measure()
			else:
				plant(Entities.Sunflower)
			if(get_ground_type() != Grounds.Soil):
				till()
			if(num_items(Items.Sunflower_Seed) < 100):
				trade(Items.Sunflower_Seed, 10)
			
		else:
			if(get_entity_type() == Entities.Sunflower) and measure() == maxsunflower:
				harvest()
				maxsunflower = 0
				plant(Entities.Sunflower)
			
		
			
	else:
		if(can_harvest()):
			harvest()
		if(get_ground_type() != Grounds.Soil):
			till()
		plant(Entities.Grass)
			
	if(num_items(Items.Water_Tank) < 5):
		trade(Items.Empty_Tank)
	if(get_water() < 0.8):
		use_item(Items.Water_Tank)
	if(get_pos_x() == 0 and get_pos_y() == 0 and j):
		j = False
	elif(get_pos_x() == 0 and get_pos_y() == 0 and j == False):
		j = True
		
	if(get_pos_y() == world):
		move(East) 
	move(North)
	