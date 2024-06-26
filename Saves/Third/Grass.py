def Grass(desired = {Items.Hay: 100}, multiple = 1):
	if Items.Hay not in desired:
		return
	amount = desired[Items.Hay] * multiple
	while True:
		world = get_world_size() -1
	
		if can_harvest():
			harvest()
			if num_items(Items.Hay) >= amount:
				return
		WaterTill()
	
		if get_entity_type() == None:
			plant(Entities.Grass)
			
		Next()
Grass({Items.Hay: 100}, 1000000)