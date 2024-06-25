def HarvestAll():
	Home()
	harvest()
	Next()
	while True:
		harvest()
		Next()
		if not get_pos_x() and not get_pos_y():
			return