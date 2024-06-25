while True:
	world = get_world_size() -1

	if can_harvest():
		harvest()
	WaterTill()

	if get_entity_type() == None:
		plant(Entities.Grass)
		
	Next()