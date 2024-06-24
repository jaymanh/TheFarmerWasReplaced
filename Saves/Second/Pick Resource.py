def PickResource(Wood = True, Carrot = True, Power = True, Pumpkin = True, Gold = True, Cactus = True, Dino = True):
	Resource = Items.Hay
	Amount = num_items(Items.Hay) - 600
	Current = Entities.Grass
	if num_items(Items.Wood) - 600 < Amount and Wood:
		Resource = Items.Wood
		Amount = num_items(Items.Wood) - 600
		Current = Entities.Tree
	if num_items(Items.Carrot) - 500 < Amount and Carrot:
		Resource = Items.Carrot
		Amount = num_items(Items.Carrot) - 500
		Current = Entities.Carrots
	if num_items(Items.Power) - 300 < Amount and Power and num_items(Items.Power) < 10000:
		Resource = Items.Power
		Amount = num_items(Items.Power) - 300
		Current = Entities.Sunflower
	if num_items(Items.Pumpkin) - 500 < Amount and Pumpkin:
		Resource = Items.Pumpkin
		Amount = num_items(Items.Pumpkin) - 500
		Current = Entities.Pumpkin
	if num_items(Items.Gold) - 300 < Amount and Gold:
		Resource = Items.Gold
		Amount = num_items(Items.Gold) - 300
		Current = None
	if num_items(Items.Cactus) + 900 < Amount and Cactus:
		Resource = Items.Cactus
		Amount = num_items(Items.Cactus) + 900
		Current = Entities.Cactus
	if num_items(Items.Bones) + 1200 < Amount and Dino:
		Resource = Items.Bones
		Amount = num_items(Items.Bones) + 1200
		Current = Entities.Dinosaur
		
	return Current