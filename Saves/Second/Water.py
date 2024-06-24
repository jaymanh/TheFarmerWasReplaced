def TryWater():
	if num_items(Items.Water_Tank) < 1 and num_unlocked(Unlocks.Trees) > 3:
		trade(Items.Empty_Tank)
	if get_water() < 0.8:
		use_item(Items.Water_Tank)