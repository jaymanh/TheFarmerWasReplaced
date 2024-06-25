def WaterTill():
	if get_ground_type() == Grounds.Turf:
		till()
	if num_items(Items.Water_Tank) < 1:
		trade(Items.Empty_Tank)
	elif get_water() < 0.8:
		use_item(Items.Water_Tank)