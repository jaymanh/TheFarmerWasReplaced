def Move_To_Next_Tile(dir):
	bX = get_world_size() #Farm width (x Boundary)
	bY = bX #Farm height (y Boundary)
	cX = get_pos_x() #Current X position
	cY = get_pos_y() #Current Y position
	
	if (dir==East):
		if (cX+1==bX):
			dir=North
	elif (dir==West):
		if (cX==0):
			dir=North
	elif (dir==North):
		if (cX+1==bX):
			dir=West
		elif (cX==0):
			dir=East
	move(dir)
	return dir
	
def Till_All():
	bX = get_world_size()
	bY = bX
	dir = East
	
	for n in range(bX*bY):
		if(get_ground_type() != Grounds.Soil):
			till()
		dir = Move_To_Next_Tile(dir)
		
def Plant_All(crop):
	bX = get_world_size()
	bY = bX
	dir = East
	Home()
	plant(crop)
	for n in range(bX*bY):
		if (get_entity_type() != crop):
			plant(crop)
		dir = Move_To_Next_Tile(dir)
		
def Do_Cactus():
	if (num_items(Items.Cactus_Seed) < 100):
		if not trade(Items.Cactus_Seed, 100):
			return
				
	Home()
	bX = get_world_size()
	bY = bX
	area = bX*bY
	sorted = 0
	dir = East
	
	HarvestAll()
	Till_All()
	Plant_All(Entities.Cactus)
	Sort_Cactuses()
	harvest()
	
def Sort_Cactuses():
	bX = get_world_size()
	bY = bX
	area = bX*bY
	sorted = 0
	dir = East
	
	while (sorted < area):
		sorted += 1
		if (Swap_Cactus_Neighbours()):
			sorted = 0
		dir = Move_To_Next_Tile(dir)
		
def Swap_Cactus_Neighbours():
	myVal = measure()
	if (myVal < measure(West) and get_pos_x() != 0):
		swap(West)
		return True
	if (myVal < measure(South) and get_pos_y() != 0):
		swap(South)
		return True
	if (myVal > measure(East) and get_pos_x() != get_world_size()-1):
		swap(East)
		return True
	if (myVal > measure(North) and get_pos_y() != get_world_size()-1):
		swap(North)
		return True
	return False #if no swap occured, don't reset sort counter
	
Do_Cactus()