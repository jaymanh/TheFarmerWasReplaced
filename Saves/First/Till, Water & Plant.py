def TryTill(Ent = Entities.Grass):
	if(num_unlocked(Unlocks.Plant) == 0):
		return
	elif(get_ground_type() == Grounds.Turf and num_unlocked(Unlocks.Carrots)):
			till()
			plant(Ent)
			if(num_items(Items.Water_Tank) < 5 and num_unlocked(Unlocks.Trees) > 0):
				trade(Items.Empty_Tank)
			if(num_items(Items.Water_Tank) != 0):
				if(get_water() < 0.8):
					use_item(Items.Water_Tank)
			return
					
	elif(get_ground_type() == Grounds.Soil):
		plant(Ent)
		if(num_items(Items.Water_Tank) < 5 and num_unlocked(Unlocks.Trees) > 0):
			trade(Items.Empty_Tank)
		if(num_items(Items.Water_Tank) != 0):
			if(get_water() < 0.8):
				use_item(Items.Water_Tank)
		return
					
	else:
		plant(Ent)
	return