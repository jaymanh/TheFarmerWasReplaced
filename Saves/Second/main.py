def main():
	harvest()
	while True:
		
		Crop = PickResource(num_unlocked(Unlocks.Trees), num_unlocked(Unlocks.Carrots),
		num_unlocked(Unlocks.Sunflowers), num_unlocked(Unlocks.Pumpkins),
		num_unlocked(Unlocks.Mazes), num_unlocked(Unlocks.Cactus), num_unlocked(Unlocks.Dinosaurs))
		Seed = Items.Carrot_Seed
		if Crop == Entities.Grass or Crop == Entities.Bush or Crop == Entities.Carrots:
			PlantAll(Crop, Seed)
			for i in range(5):
				FarmAll(Crop, Seed)
		elif Crop == Entities.Tree:
			PlantAllTree()
			for i in range(5):
				FarmAllTree()
		elif Crop == Entities.Sunflower:
			for i in range(2):
				Power()
		elif Crop == Entities.Pumpkin:
			for i in range(5):
				Pumpkin()
		elif Crop == None:
			for i in range(2):
				Maze()
		elif Crop == Entities.Cactus:
			for i in range(5):
				Do_Cactus()
		elif Crop == Entities.Dinosaur:
			for i in range(10):
				DinoAll()
				HarvestAll()
		if unlock(Unlocks.Leaderboard):
			timed_reset()
		if num_unlocked(Unlocks.Dinosaurs) < 2:
			unlock(Unlocks.Dinosaurs)
		if num_unlocked(Unlocks.Mazes) < 1:
			unlock(Unlocks.Mazes)
		unlock(Unlocks.Speed)
		if num_unlocked(Unlocks.Dinosaurs) < 2:
			TempAUnlock()
main()