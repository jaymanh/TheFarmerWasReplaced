def NewWood(j = {Items.Wood: 1000}):
	world = get_world_size()
	i = 0
	if Items.Wood not in j:
		return
	k = j[Items.Wood]
	if k == 0:
		return
	if k < 100:
		k = 100
	while(i < k):
		if(can_harvest() and get_entity_type() != Entities.Grass):
			harvest()
			i +=1
			
		if(get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0) or (get_pos_x() % 2 != 0 and get_pos_y() % 2 !=0):
			TryTill(Entities.Tree)
		
		if(num_unlocked(Unlocks.Expand) > 1) and num_unlocked(Unlocks.Senses):
			move(North)
			if(get_pos_y() == world -1):
				if(can_harvest() and get_entity_type() != Entities.Grass):
					harvest()
					i +=1
				if(get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0) or (get_pos_x() % 2 != 0 and get_pos_y() % 2 !=0):
					TryTill(Entities.Tree)
				move(East)
				move(North)
NewWood()