def Carrots():
	while True:
		world = get_world_size() -1
		if can_harvest():
			harvest()
		WaterTill()
		
		if num_items(Items.Carrot_Seed) < 5:
			trade(Items.Carrot_Seed, 20)
		if get_ground_type() == Grounds.Turf:
			till()
		if get_entity_type() == None:
			plant(Entities.Carrots)
			
		Next()
Carrots()