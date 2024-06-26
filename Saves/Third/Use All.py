def UseAll(item = Items.Egg):
	if num_items(item) < 5:
		Buy(item, 100)
	use_item(item)
	Next()
	while True:
		use_item(item)
		Next()
		if num_items(item) < 5:
			Buy(item, 100)
		if not get_pos_x() and not get_pos_y():
			return