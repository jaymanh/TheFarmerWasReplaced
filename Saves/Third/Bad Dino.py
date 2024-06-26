def Dino(desired = {Items.Bones: 100}, multiple = 1):
	if Items.Bones not in desired:
		return
	amount = desired[Items.Bones] * multiple
	while amount > num_items(Items.Bones):
		clear()
		UseAll()
		HarvestAll()
Dino({Items.Bones: 100}, 100000000)