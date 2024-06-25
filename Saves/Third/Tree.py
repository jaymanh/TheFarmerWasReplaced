def Tree():	
	while True:
		world = get_world_size() -1
		
		if can_harvest():
			harvest()
		WaterTill()
		
		if get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0 and get_entity_type() == None:
			plant(Entities.Tree)
		elif (get_pos_x() + 1) % 2 == 0 and (get_pos_y() + 1) % 2 == 0 and get_entity_type() == None:
			plant(Entities.Tree)
		
		Next()
Tree()