def BuyUnlcok(Tech = Unlocks.Speed):
	if not unlock(Tech):
		cost = get_cost(Tech)
		Grass(cost)
		Tree(cost)
		Carrots(cost)
		Pumpkin(cost)
		Maze(cost)
		Cactus(cost)
		Dino(cost)
		BuyUnlcok(Tech)