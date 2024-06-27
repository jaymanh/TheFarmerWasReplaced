def PlantAll(Crop = Entities.Pumpkin, Seed = Items.Pumpkin_Seed, Water = True):
	Home()
	if num_items(Seed) < 5:
		Buy(Seed, 20)
	harvest()
	WaterTill(Water)
	plant(Crop)
	Next()
	while True:
		harvest()
		WaterTill(Water)
		if num_items(Seed) < 5:
			Buy(Seed, 20)
		plant(Crop)
		Next()
		if not get_pos_x() and not get_pos_y():
			return
PlantAll()