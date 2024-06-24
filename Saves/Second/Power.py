def Power():
	HarvestAll()
	Home()
	reset = 0
	world = get_world_size() - 1
	bX = get_world_size()
	bY = bX
	first = True
	listSFH = []
	last = 15
	a = 0
	while a < 4:
		if num_items(Items.Sunflower_Seed) < 100:
			if not trade(Items.Sunflower_Seed, 100):
				return
	
		if get_ground_type() == Grounds.Turf:
			till()
		plant(Entities.Sunflower)
		TryWater()
				
		listSFH.append([get_pos_x(), get_pos_y(), measure()])
		if(get_pos_y() == world):
			
			move(East)
			move(North)
			if(get_pos_x() == 0 and get_pos_y() == 0):
				while last > 8:
					for i in listSFH:
						if i[2] == last:
							GoTo(i[0], i[1])
							harvest() 
					last -= 1
				last = 15
				reset += 1
				if reset > 1:
					for j in listSFH:
						if j[2] == 7:
							GoTo(j[0], j[1])
							harvest()
							a += 1
							reset = 0
							break
				listSFH = []
				Home()
			if get_ground_type() == Grounds.Turf:
				till()
			plant(Entities.Sunflower)
			TryWater()
				
			listSFH.append([get_pos_x(), get_pos_y(), measure()])
		
		move(North)
Power()