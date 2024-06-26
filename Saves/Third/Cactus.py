def Cactus(desired = {Items.Cactus: 100}, multiple = 1):
	if Items.Cactus not in desired:
		return
	amount = desired[Items.Cactus] * multiple
	clear()
	seeds = get_world_size() * get_world_size() + 20
	while amount > num_items(Items.Cactus):
		if (num_items(Items.Cactus_Seed) < seeds):
			Buy(Items.Cactus_Seed, seeds)
		PlantAll(Entities.Cactus, Items.Cactus_Seed)
		Sort_Cactuses()
		harvest()
	
def Sort_Cactuses():
	area = get_world_size()*get_world_size()
	sorted = 0
	
	while (sorted < area):
		sorted += 1
		if (Swap_Cactus_Neighbours()):
			sorted = 0
		Next()
		
def Swap_Cactus_Neighbours():
	Curr = measure()
	if (Curr < measure(West) and get_pos_x() != 0):
		swap(West)
		return True
	if (Curr < measure(South) and get_pos_y() != 0):
		swap(South)
		return True
	if (Curr > measure(East) and get_pos_x() != get_world_size()-1):
		swap(East)
		return True
	if (Curr > measure(North) and get_pos_y() != get_world_size()-1):
		swap(North)
		return True
	return False
	
Cactus({Items.Cactus: 100}, 1000000)