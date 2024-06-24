def FarmDino():
	if num_items(Items.Cactus) < 10000:
		FarmCactus()
		return
	untillAll()
	HarvestAll()
	Home()
	i = 0
	while(i < 10):
		if(num_items(Items.Egg) < 200):
			trade(Items.Egg,100)
		UseAll(Items.Egg)
		HarvestAll()
		i += 1
	unlock(Unlocks.Leaderboard)
	if(num_unlocked(Unlocks.Leaderboard)):
		timed_reset()
	
def UseAll(Item):
	bX = get_world_size()
	bY = bX
	world = get_world_size()
	for n in range(bX*bY):
		use_item(Item)
		if(get_pos_y() == world - 1):	
			move(East)
		move(North)
		
FarmDino()