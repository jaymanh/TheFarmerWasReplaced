def Run():
	while True:
		Resourse = GetResource(num_unlocked(Unlocks.Trees),
		num_unlocked(Unlocks.Carrots), num_unlocked(Unlocks.Pumpkins),
		num_unlocked(Unlocks.Sunflowers), num_unlocked(Unlocks.Mazes),
		num_unlocked(Unlocks.Cactus), num_unlocked(Unlocks.Dinosaurs))
		amount = num_items(Resourse) * 1.5
		if Resourse == Items.Hay:
			Grass({Items.Hay: 1}, amount)
		elif Resourse == Items.Wood:
			Tree({Items.Wood: 1}, amount)
		elif Resourse == Items.Carrot:
			Carrots({Items.Carrot: 1}, amount) 
		elif Resourse == Items.Pumpkin:
			Pumpkin({Items.Pumpkin: 1}, amount)
		elif Resourse == Items.Power:
			Power(amount)
		elif Resourse == Items.Gold:
			Maze({Items.Gold: 1}, amount)
		elif Resourse == Items.Cactus:
			Cactus({Items.Cactus: 1}, amount)
		else:
			Dino({Items.Bones: 1}, amount)
Run()