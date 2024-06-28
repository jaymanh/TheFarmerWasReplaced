def TreePoly(desired = {Items.Wood: 100}, multiple = 1):
	if Items.Wood not in desired:
		return
	amount = desired[Items.Wood] * multiple
	poly_list = []
	while True:
		world = get_world_size() -1
		
		if can_harvest():
			harvest()
			if num_items(Items.Wood) >= amount:
				return
		WaterTill()
		
		for t in poly_list:
			if t[1] == get_pos_x() and t[2] == get_pos_y():
				if t[0] == Entities.Carrots and num_items(Items.Carrot_Seed) < 5:
					Buy(Items.Carrot_Seed, 20)
				plant(t[0])
				poly_list.remove(t)
				break
		
		if get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0 and get_entity_type() == None:
			plant(Entities.Tree)
		elif get_pos_x() % 2 and get_pos_y() % 2 and get_entity_type() == None:
			plant(Entities.Tree)
		if get_companion() != None:
			poly_list.append(get_companion())
		
		Next()
TreePoly({Items.Wood: 100}, 10000000000)