def Carrots(desired = {Items.Carrot: 100}, multiple = 1):
	if Items.Carrot not in desired:
		return
	amount = desired[Items.Carrot] * multiple
	while True:
		if can_harvest():
			harvest()
			if num_items(Items.Carrot) >= amount:
				return
		WaterTill()
		
		if num_items(Items.Carrot_Seed) < 5:
			Buy(Items.Carrot_Seed, 80)
		if get_entity_type() == None:
			plant(Entities.Carrots)
			
		Next()
Carrots({Items.Carrot: 100}, 100000000)