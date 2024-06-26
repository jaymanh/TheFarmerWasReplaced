def Tree(desired = {Items.Wood: 100}, multiple = 1):
	if Items.Wood not in desired:
		return
	amount = desired[Items.Wood] * multiple
	while True:
		world = get_world_size() -1
		
		if can_harvest():
			harvest()
			if num_items(Items.Wood) >= amount:
				return
		WaterTill()
		
		if get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0 and get_entity_type() == None:
			plant(Entities.Tree)
		elif get_pos_x() % 2 and get_pos_y() % 2 and get_entity_type() == None:
			plant(Entities.Tree)
		
		Next()
Tree({Items.Wood: 100}, 10000000000)