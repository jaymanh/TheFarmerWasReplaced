def Pumpkin():
	HarvestAll()
	Till_All()
	PlantAll(Entities.Pumpkin, Items.Pumpkin_Seed)
	Home()
	world = get_world_size() - 1
	bX = get_world_size()
	bY = bX
	Unchecked = []
	while True:
		if num_items(Items.Pumpkin_Seed) < 100:
			if not trade(Items.Pumpkin_Seed, 100):
				return
	
		if get_ground_type() == Grounds.Turf:
			till()
		if not can_harvest() and get_entity_type() == Entities.Pumpkin:
			Unchecked.append([get_pos_x(), get_pos_y(), None])
		else:
			Unchecked.append([get_pos_x(), get_pos_y(), get_entity_type()])
		plant(Entities.Pumpkin)
		TryWater()
		if(get_pos_y() == world):
			move(East)
			move(North)
			
			if(get_pos_x() == 0 and get_pos_y() == 0):
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
						do_a_flip()
						harvest()
						return
					Unchecked = TempList
					
					
			if get_ground_type() == Grounds.Turf:
				till()
			if not can_harvest() and get_entity_type() == Entities.Pumpkin:
				Unchecked.append([get_pos_x(), get_pos_y(), None])
			else:
				Unchecked.append([get_pos_x(), get_pos_y(), get_entity_type()])
			plant(Entities.Pumpkin)
			TryWater()
		
		move(North)
		
while True:
	Pumpkin()