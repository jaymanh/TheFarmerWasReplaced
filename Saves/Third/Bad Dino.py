def Dino(desired = {Items.Bones: 100}, multiple = 1):
	if Items.Bones not in desired:
		return
	Buy(Items.Egg, 100)	
	amount = desired[Items.Bones] * multiple
	HarvestAll()
	while amount > num_items(Items.Bones):
		UseAll()
		HarvestAll()
Dino({Items.Bones: 100}, 100000000)