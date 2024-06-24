def NewHay(j = {Items.Hay: 100}):
	world = get_world_size()
	i = 0
	if Items.Hay not in j:
		return
	k = j[Items.Hay]
	if k == 0:
		return
	if k < 100 and num_unlocked(Unlocks.Expand) > 1:
		k = 100
	while(i < k):
		if(can_harvest()):
			harvest()
			i +=1
			
		TryTill(Entities.Grass)
		
		if(num_unlocked(Unlocks.Expand) == 1):
			move(North)
			
		elif(num_unlocked(Unlocks.Expand) > 1) and num_unlocked(Unlocks.Senses):
			move(North)
			if(get_pos_y() == world -1):
				if(can_harvest()):
					harvest()
					i +=1
				TryTill(Entities.Grass)
				move(East)
				move(North)	
NewHay()