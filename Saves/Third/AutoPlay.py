def Autoplay():
	ulist = [Unlocks.Trees, Unlocks.Expand, Unlocks.Speed, Unlocks.Carrots, Unlocks.Sunflowers, Unlocks.Trees, Unlocks.Grass, 
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
	poweroff = 1.1
	for curunlock in ulist:
		if num_unlocked(Unlocks.Sunflowers) and num_items(Items.Power) < (100 * poweroff):
			Power(200 * poweroff)
			poweroff += 0.2
		BuyUnlock(curunlock)
		if poly and num_unlocked(Unlocks.Polyculture) == 1:
			quick_print("Polly: ", get_time() - Start_time)
			poly = False
		if maze and num_unlocked(Unlocks.Mazes) == 1:
			quick_print("Mazes: ", get_time() - Start_time)
			maze = False
		if dino and num_unlocked(Unlocks.Dinosaurs) == 1:
			quick_print("Dino: ", get_time() - Start_time)
			Power(700)
			dino = False
	quick_print("Fin: ", get_time() - Start_time)
	timed_reset()