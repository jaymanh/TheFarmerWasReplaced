def Autoplay():
	list  = [Unlocks.Trees, Unlocks.Expand, Unlocks.Speed, Unlocks.Carrots, Unlocks.Sunflowers, Unlocks.Trees, Unlocks.Grass, 
	Unlocks.Speed, Unlocks.Grass, Unlocks.Carrots, Unlocks.Speed, Unlocks.Carrots, Unlocks.Speed, Unlocks.Pumpkins, Unlocks.Polyculture,
	Unlocks.Speed, Unlocks.Speed, Unlocks.Speed, Unlocks.Carrots, Unlocks.Pumpkins, Unlocks.Pumpkins, Unlocks.Pumpkins, Unlocks.Expand,
	Unlocks.Expand, Unlocks.Expand, Unlocks.Speed, Unlocks.Speed, Unlocks.Speed, Unlocks.Trees, Unlocks.Carrots, Unlocks.Pumpkins,
	Unlocks.Pumpkins, Unlocks.Expand, Unlocks.Expand, Unlocks.Speed, Unlocks.Speed, Unlocks.Trees,
	Unlocks.Carrots, Unlocks.Pumpkins, Unlocks.Pumpkins, Unlocks.Expand, Unlocks.Fertilizer, Unlocks.Mazes, Unlocks.Mazes, Unlocks.Mazes,
	Unlocks.Cactus, Unlocks.Cactus, Unlocks.Cactus, Unlocks.Dinosaurs, Unlocks.Dinosaurs, Unlocks.Leaderboard]
	Start_time = get_time()
	poly = True
	maze = True
	dino = True
	for unlock in list:
		if num_unlocked(Unlocks.Sunflowers) > 0 and num_items(Items.Power) < 500:
			Power(1000)
		BuyUnlock(unlock)
		if poly and num_unlocked(Unlocks.Polyculture) == 1:
			quick_print("Polly: ", get_time() - Start_time)
			poly = False
		if maze and num_unlocked(Unlocks.Mazes) == 1:
			quick_print("Mazes: ", get_time() - Start_time)
			maze = False
		if dino and num_unlocked(Unlocks.Dinosaurs) == 1:
			quick_print("Dino: ", get_time() - Start_time)
			dino = False
	quick_print("Fin: ", get_time() - Start_time)
	timed_reset()