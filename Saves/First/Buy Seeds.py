def BuySeeds(seed = Items.Carrot_Seed):
	if (num_items(seed) < 100):
		if(not trade(seed,100)):
			NewHay(get_cost(seed))
			if(num_unlocked(Unlocks.Trees)):
				NewWood(get_cost(seed))
			else:
				NewBush(get_cost(seed))
			NewCarrot(get_cost(seed))
			NewPumpkin(get_cost(seed))
			return False
	return True