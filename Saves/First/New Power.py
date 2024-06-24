def NewPower(j = {Items.Power: 2000}):
	HarvestAll()
	Home()
	world = get_world_size() -1 
	if Items.Power not in j:
		return
	k = j[Items.Power]
	if k == 0:
		return
	if k < 100:
		k = 100
	reset = 0
	bX = get_world_size()
	bY = bX
	first = True
	listSFH = []
	last = 15
	while(num_items(Items.Power) < k):
		if num_items(Items.Sunflower_Seed) < 200:
			if not BuySeeds(Items.Sunflower_Seed):
				return

		
		TryTill(Entities.Sunflower)	
		listSFH.append([get_pos_x(), get_pos_y(), measure()])
		if(get_pos_y() == world):
			
			move(East)
			move(North)
			if(get_pos_x() == 0 and get_pos_y() == 0):
				while last > 9:
					for i in listSFH:
						if i[2] == last:
							GoTo(i[0], i[1])
							harvest() 
					last -= 1
				listSFH = []
				last = 15
				reset += 1
				if reset > 3:
					HarvestAll()
					reset = 0
				Home()
			TryTill(Entities.Sunflower)
			listSFH.append([get_pos_x(), get_pos_y(), measure()])
		
		move(North)
NewPower({Items.Power: 100000})