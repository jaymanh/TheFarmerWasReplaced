while(True):
	farm = FindResource(True)
	if(farm == Items.Hay):
		FarmHay()
	elif(farm == Items.Carrot):
		FarmCarrot()
	elif(farm == Items.Wood):
		FarmWood()
	elif(farm == Items.Pumpkin):
		FarmPumkin()
	elif(farm == Items.Power):
		FarmPower()
	elif(farm == Items.Gold):
		FarmGold()
	elif(farm == Items.Cactus):
		FarmCactus()
	else:
		FarmDino()