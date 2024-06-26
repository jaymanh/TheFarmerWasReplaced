def CarrotPoly(desired = {Items.Carrot: 100}, multiple = 1):
	if Items.Carrot not in desired:
		return
	amount = desired[Items.Carrot] * multiple
	poly_list = []
	while True:	
		if can_harvest():
			harvest()
			if num_items(Items.Carrot) >= amount:
				return
		WaterTill()

		for t in poly_list:
			if t[1] == get_pos_x() and t[2] == get_pos_y():
				if t[0] == Entities.Carrots and num_items(Items.Carrot_Seed) < 5:
					Buy(Items.Carrot_Seed, 20)
				plant(t[0])
				poly_list.remove(t)
				break
		if num_items(Items.Carrot_Seed) < 5:
			Buy(Items.Carrot_Seed, 20)	
		if get_entity_type() == None:
			plant(Entities.Carrots)
		if get_companion() != None:
			poly_list.append(get_companion())
			
		Next()
		
CarrotPoly({Items.Carrot: 100}, 1000000)