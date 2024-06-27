def BuyUnlock(Tech = Unlocks.Speed):
	if not unlock(Tech):
		cost = get_cost(Tech)
		Dino(cost)
		Cactus(cost)
		Maze(cost)
		Pumpkin(cost)
		Carrots(cost)
		Tree(cost)
		Grass(cost)
		if Items.Power in cost:
			amount = cost[Items.Power] * 1.5
			Power(amount) 
		BuyUnlock(Tech)