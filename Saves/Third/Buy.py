def Buy(Item = Items.Carrot_Seed, Amount = 10):
	a = True
	if not trade(Item, Amount): 
		a = False
		cost = get_cost(Item)
		Grass(cost, Amount)
		Tree(cost, Amount)
		Carrots(cost, Amount)
		Pumpkin(cost, Amount)
		Maze(cost, Amount)
		Cactus(cost, Amount)
		Dino(cost, Amount)
		Buy(Item, Amount)
	return a
		