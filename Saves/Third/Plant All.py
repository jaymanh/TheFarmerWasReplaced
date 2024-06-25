def PlantAll(Crop = {Items.Wheet: 100}):
	if Items.Wheet not in Crop and Items.Carrot not in Crop and Items.Wood not in Crop:
		return
	Seed = None
	if Items.Carrot in Crop:
		Seed = Items.Carrot_Seed
	
	Home()
	trade(Seed, 20)
	harvest()
	WaterTill()
	plant(Crop)
	Next()
	while True:
		harvest()
		WaterTill()
		if num_items(Seed) < 5:
			trade(Seed, 20)
		plant(Crop)
		Next()
		if not get_pos_x() and not get_pos_y():
			return
PlantAll()