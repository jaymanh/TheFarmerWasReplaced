def WaterTill():
	if get_ground_type() == Grounds.Turf and num_unlocked(Unlocks.Carrots):
		till()
	if num_items(Items.Water_Tank) < 1 and num_unlocked(Unlocks.Carrots):
		trade(Items.Empty_Tank)
	elif num_unlocked(Unlocks.Carrots):
		if get_water() < 0.8:
			use_item(Items.Water_Tank)