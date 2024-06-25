def Pumpkin():
	PlantAll(Entities.Pumpkin, Items.Pumpkin_Seed)
	Home()
	Unchecked = []
	while True:
		if num_items(Items.Pumpkin_Seed) < 100:
			if not trade(Items.Pumpkin_Seed, 100):
				return
			
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
					return
				Unchecked = TempList		
a = get_time()
b = num_items(Items.Pumpkin)
while get_time() - a < 60:
	Pumpkin()
print(get_time() - a)
print(num_items(Items.Pumpkin) - b)