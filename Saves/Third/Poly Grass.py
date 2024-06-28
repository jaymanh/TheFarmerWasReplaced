def GrassPoly(desired = {Items.Hay: 100}, multiple = 1):
	if Items.Hay not in desired:
		return
	amount = desired[Items.Hay] * multiple
	poly_list = []
	while True:	
		if can_harvest():
			harvest()
			if num_items(Items.Hay) >= amount:
				return
		WaterTill()

		for t in poly_list:
			if t[1] == get_pos_x() and t[2] == get_pos_y():
				if t[0] == Entities.Carrots and num_items(Items.Carrot_Seed) < 5:
					Buy(Items.Carrot_Seed, 20)
				plant(t[0])
				poly_list.remove(t)
				break
				
		if get_entity_type() == None:
			plant(Entities.Grass)
		if get_companion() != None:
			poly_list.append(get_companion())
			
		Next()
		
GrassPoly({Items.Hay: 100}, 1000000)