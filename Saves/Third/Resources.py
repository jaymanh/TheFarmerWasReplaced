def GetResource(Tree = True, Carrots = True, Pumpkin = True, Power = True, Gold = True, Cactus = True, Dino = True):
	Current = Items.Hay
	Amount = num_items(Items.Hay)
	if num_items(Items.Wood) < Amount and Tree:
		Current = Items.Wood
		Amount = num_items(Current)
	if num_items(Items.Carrot) < Amount and Carrots:
		Current = Items.Carrot
		Amount = num_items(Current)
	if num_items(Items.Pumpkin) < Amount and Pumpkin:
		Current = Items.Pumpkin
		Amount = num_items(Current)
	if num_items(Items.Power) < Amount and Power:
		Current = Items.Power
		Amount = num_items(Current)
	if num_items(Items.Gold) < Amount and Gold:
		Current = Items.Gold
		Amount = num_items(Current)
	if num_items(Items.Cactus) < Amount and Cactus:
		Current = Items.Cactus
		Amount = num_items(Current)
	if num_items(Items.Bones) < Amount and Dino:
		Current = Items.Bones
		Amount = num_items(Current)
	return Current