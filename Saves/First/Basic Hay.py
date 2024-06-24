def BasicHay(j = {Items.Hay: 100}):
	i = 0 
	k = j[Items.Hay]
	while i < k:
		if can_harvest():
			harvest()
			i += 1
		move(North)
BasicHay()