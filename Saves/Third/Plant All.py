def PlantAll(Crop = Entities.Carrots, Seed = Items.Carrot_Seed):
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