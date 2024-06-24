def NewCarrot(j = {Items.Carrot: 1000}):
	world = get_world_size()
	i = 0
	if Items.Carrot not in j:
		return
	k = j[Items.Carrot]
	if k == 0:
		return
	if k < 100:
		k = 100
	while(i < k):
		if num_items(Items.Carrot_Seed) < 100:
			if not BuySeeds(Items.Carrot_Seed):
				return
		if(can_harvest() and get_entity_type() != Entities.Grass):
			harvest()
			i +=1
			
		TryTill(Entities.Carrots)
		
		if(num_unlocked(Unlocks.Expand) == 1):
			move(North)
			
		elif(num_unlocked(Unlocks.Expand) > 1) and num_unlocked(Unlocks.Senses):
			move(North)
			if(get_pos_y() == world -1):
				if(can_harvest() and get_entity_type() != Entities.Grass):
					harvest()
					i +=1
				TryTill(Entities.Carrots)
				move(East)
				move(North)	
	unlock(Unlocks.Speed)
	if num_unlocked(Unlocks.Sunflowers) == 0:
		unlock(Unlocks.Sunflowers)
	
NewCarrot()