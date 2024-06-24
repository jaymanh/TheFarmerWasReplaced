def NewPumpkin(j = {Items.Pumpkin: 10000}):
	HarvestAll()
	Home()
	world = get_world_size() -1 
	i = num_items(Items.Pumpkin)
	if Items.Pumpkin not in j:
		return
	k = j[Items.Pumpkin]
	if k == 0:
		return
	if k < 100:
		k = 100
		
	bX = get_world_size()
	bY = bX
	while(num_items(Items.Pumpkin) - i < k):
		if num_items(Items.Pumpkin_Seed) < 200:
			if not BuySeeds(Items.Pumpkin_Seed):
				return

		if(get_entity_type() != Entities.Pumpkin):
			emptySpace = True
		
		TryTill(Entities.Pumpkin)	
		
		if(get_pos_y() == world):
			
			if(get_pos_x() == world and get_pos_y() == world and emptySpace == False):
				harvest()
			move(East)
			move(North)
			if(get_pos_x() == 0 and get_pos_y() == 0):
				emptySpace = False
			TryTill(Entities.Pumpkin)
		
		move(North)
	if(num_unlocked(Unlocks.Dinosaurs) < 1):
		unlock(Unlocks.Dinosaurs)
				
NewPumpkin({Items.Pumpkin: 1000000})