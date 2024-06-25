def Grass(desired = {Items.Hay: 100}):
	if Items.Hay not in desired:
		return
	while True:
		world = get_world_size() -1
	
		if can_harvest():
			harvest()
			if num_items(Items.Hay) >= desired[Items.Hay]:
				return
		WaterTill()
	
		if get_entity_type() == None:
			plant(Entities.Grass)
			
		Next()
Grass()