def Start():
	Start_time = get_time()
	timed_reset()
	for i in range(101):
		harvest()
	unlock(Unlocks.Grass)
	for i in range(10):
		harvest()
	unlock(Unlocks.Speed)
	while num_items(Items.Hay) < 30:
		if can_harvest():
			harvest()
	unlock(Unlocks.Expand)
	while num_items(Items.Hay) < 50:
		harvest()
		move(North)
	unlock(Unlocks.Plant)
	while num_items(Items.Wood) < 20:
		if can_harvest():
			harvest()
			plant(Entities.Bush)
		move(North)
	unlock(Unlocks.Expand)
	while num_items(Items.Wood) < 10:
		if can_harvest():
			harvest()
			plant(Entities.Bush)
		Next()
	unlock(Unlocks.Speed)
	while num_items(Items.Hay) < 300:
		if can_harvest():
			harvest()
		Next()
	unlock(Unlocks.Grass)
	while num_items(Items.Wood) < 211:
		if can_harvest():
			harvest()
			plant(Entities.Bush)
		Next()
	while num_items(Items.Hay) < 70:
		if can_harvest():
			harvest()
		Next()
	unlock(Unlocks.Carrots)
	trade(Items.Carrot_Seed, 70)
	while num_items(Items.Carrot) < 200:
		if can_harvest():
			harvest()
		if get_ground_type() ==  Grounds.Turf:
			till()
		plant(Entities.Carrots)
		Next()
	unlock(Unlocks.Trees)
	quick_print("Early Game: ", get_time() - Start_time)
	Autoplay()
	
Start()
