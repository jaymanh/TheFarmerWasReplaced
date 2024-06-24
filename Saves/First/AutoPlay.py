def AutoPlay():
	timed_reset()
	BasicHay(get_cost(Unlocks.Speed))
	unlock(Unlocks.Speed)
	BasicHay(get_cost(Unlocks.Expand))
	unlock(Unlocks.Expand)
	BasicHay(get_cost(Unlocks.Plant))
	unlock(Unlocks.Plant)
	NewBush(get_cost(Unlocks.Expand))
	unlock(Unlocks.Expand)
	
	
	while(True):
		farm = FindResource(True,
		num_unlocked(Unlocks.Carrots), num_unlocked(Unlocks.Pumpkins),
		#False, False,
		num_unlocked(Unlocks.Sunflowers), 
		#False,
		num_unlocked(Unlocks.Mazes), 
		num_unlocked(Unlocks.Cactus), num_unlocked(Unlocks.Dinosaurs))
		
		TryUnlock()
		
		if(farm == Items.Hay):
			NewHay()
		elif(farm == Items.Carrot):
			NewCarrot()
		elif(farm == Items.Wood):
			if(num_unlocked(Unlocks.Trees)):
				NewWood()
			else:
				NewBush()
		elif(farm == Items.Pumpkin):
			NewPumpkin()
		elif(farm == Items.Power):
			if num_unlocked(Unlocks.Mazes) > 0:
				NewPower({Items.Power: 4000})
			else:
				NewPower()
		elif(farm == Items.Gold):
			FarmGold()
		elif(farm == Items.Cactus):
			FarmCactus()
		else:
			FarmDino()
	