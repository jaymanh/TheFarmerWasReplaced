def NewBush(j = {Items.Wood: 100}):
	world = get_world_size()
	i = 0
	if Items.Wood not in j:
		return
	k = j[Items.Wood]
	if k == 0:
		return
	if k < 100 and num_unlocked(Unlocks.Expand) > 1:
		k = 100
	while(i < k):
		if(can_harvest() and get_entity_type() != Entities.Grass):
			harvest()
			i +=1
			
		TryTill(Entities.Bush)
		
		if(num_unlocked(Unlocks.Expand) == 1):
			move(North)
			
		if(num_unlocked(Unlocks.Expand) > 1) and num_unlocked(Unlocks.Senses):
			move(North)
			if(get_pos_y() == world -1):
				if(can_harvest() and get_entity_type() != Entities.Grass):
					harvest()
					i +=1
				TryTill(Entities.Bush)
				move(East)
				move(North)	
NewBush()