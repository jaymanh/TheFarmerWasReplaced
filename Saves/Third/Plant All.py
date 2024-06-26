def PlantAll(Crop = Entities.Pumpkin, Seed = Items.Pumpkin_Seed):
	Home()
	if num_items(Seed) < 5:
		Buy(Seed, 20)
	harvest()
	WaterTill()
	plant(Crop)
	Next()
	while True:
		harvest()
		WaterTill()
		if num_items(Seed) < 5:
			Buy(Seed, 20)
		plant(Crop)
		Next()
		if not get_pos_x() and not get_pos_y():
			return
PlantAll()