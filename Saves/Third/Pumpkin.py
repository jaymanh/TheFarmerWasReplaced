def Pumpkin(desired = {Items.Pumpkin: 100}, multiple = 1):
	if Items.Pumpkin not in desired:
		return
	amount = desired[Items.Pumpkin] * multiple
	PlantAll()
	Home()
	Unchecked = []
	if num_items(Items.Pumpkin_Seed) < 100:
			Buy(Items.Pumpkin_Seed, 200)
			HarvestAll()
	while True:			
		if not can_harvest() and get_entity_type() == Entities.Pumpkin:
			Unchecked.append([get_pos_x(), get_pos_y(), None])
		else:
			Unchecked.append([get_pos_x(), get_pos_y(), get_entity_type()])

		WaterTill()
		plant(Entities.Pumpkin)
		Next()
			
		if not get_pos_x()and not get_pos_y():
			while True:
				TempList = []
				b = 0
				for i in Unchecked:
					if i[2] == None:
						GoTo(i[0], i[1])
						if not can_harvest() and get_entity_type() == Entities.Pumpkin:
							TempList.append([get_pos_x(), get_pos_y(), None])
						TempList.append([get_pos_x(), get_pos_y(), get_entity_type()])
						if get_entity_type() == None or not can_harvest():
							b += 1
						plant(Entities.Pumpkin)
						
				if b == 0:	
					Home()
					harvest()
					if num_items(Items.Pumpkin_Seed) < 140:
						if not Buy(Items.Pumpkin_Seed, 200):
							HarvestAll()
					if num_items(Items.Pumpkin) >= amount:
						return
					Unchecked = []
					TempList = []
					PlantAll()
					break
				Unchecked = TempList		

Pumpkin({Items.Pumpkin: 100}, 1000000000)