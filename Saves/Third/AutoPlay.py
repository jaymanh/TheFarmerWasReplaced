def Autoplay():
	list  = [Unlocks.Trees, Unlocks.Expand, Unlocks.Speed, Unlocks.Carrots, Unlocks.Sunflowers, Unlocks.Trees, Unlocks.Grass, 
	Unlocks.Speed, Unlocks.Grass, Unlocks.Carrots, Unlocks.Speed, Unlocks.Carrots, Unlocks.Speed, Unlocks.Pumpkins, 
	#Unlocks.Polyculture,
	Unlocks.Speed, Unlocks.Speed, Unlocks.Speed, Unlocks.Carrots, Unlocks.Pumpkins, Unlocks.Pumpkins, Unlocks.Pumpkins, Unlocks.Expand,
	Unlocks.Expand, Unlocks.Expand, Unlocks.Speed, Unlocks.Speed, Unlocks.Speed, Unlocks.Trees, Unlocks.Carrots, Unlocks.Pumpkins,
	Unlocks.Pumpkins, Unlocks.Expand, Unlocks.Expand, Unlocks.Speed, Unlocks.Speed, Unlocks.Trees,
	Unlocks.Carrots, Unlocks.Pumpkins, Unlocks.Pumpkins, Unlocks.Expand, Unlocks.Fertilizer, Unlocks.Mazes, Unlocks.Mazes, Unlocks.Mazes,
	Unlocks.Cactus, Unlocks.Cactus, Unlocks.Cactus, Unlocks.Dinosaurs, Unlocks.Dinosaurs, Unlocks.Leaderboard]
	for unlock in list:
		if num_unlocked(Unlocks.Sunflowers) > 0 and num_items(Items.Power) < 500:
			Power(1000)
		BuyUnlock(unlock)
	timed_reset()