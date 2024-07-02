def Buy(Item = Items.Carrot_Seed, Amount = 10):
	a = True
	if not trade(Item, Amount): 
		a = False
		cost = get_cost(Item)
		Dino(cost, Amount)
		Cactus(cost, Amount)
		Maze(cost, Amount)
		Pumpkin(cost, Amount)
		if num_unlocked(Unlocks.Polyculture):
			CarrotPoly(cost, Amount)
			TreePoly(cost, Amount)
			GrassPoly(cost, Amount)
		else:
			Carrots(cost, Amount)
			Tree(cost, Amount, Entities.Grass)
			Grass(cost, Amount)
		Buy(Item, Amount)
	return a
		