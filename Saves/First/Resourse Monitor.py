def FindResource(wood = True, carrot = True, pumkin = True ,power = True, gold = True, cactus = True, bones = True):
	current = Items.Hay
	amount = num_items(Items.Hay)
	
	if(num_items(Items.Wood) < amount and wood):
		current = Items.Wood
		amount = num_items(Items.Wood)
	if(num_items(Items.Carrot) < amount and carrot):
		current = Items.Carrot
		amount = num_items(Items.Carrot)
	if(num_items(Items.Pumpkin) < amount and pumkin):
		current = Items.Pumpkin
		amount = num_items(Items.Pumpkin)
	if(num_items(Items.Power) < amount and power and num_items(Items.Power) < 1000):
		current = Items.Power
		amount = num_items(Items.Power)
	if(num_items(Items.Gold) < amount and gold):
		current = Items.Gold
		amount = num_items(Items.Gold)
	if(num_items(Items.Cactus) < amount and cactus):
		current = Items.Cactus
		amount = num_items(Items.Cactus)
	if(num_items(Items.Bones) < amount and bones):
		current = Items.Bones
		amount = num_items(Items.Bones)
		
	return current