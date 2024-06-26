def BuyUnlock(Tech = Unlocks.Speed):
	if not unlock(Tech):
		cost = get_cost(Tech)
		Grass(cost)
		Tree(cost)
		Carrots(cost)
		Pumpkin(cost)
		Maze(cost)
		Cactus(cost)
		Dino(cost)
		if Items.Power in cost:
			amount = cost[Items.Power] * 1.5
			Power(amount) 
		BuyUnlock(Tech)