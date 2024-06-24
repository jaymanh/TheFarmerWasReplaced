timed_reset()
while True:
	harvest()
	if num_items(Items.Hay) == 20:
		unlock(Unlocks.Speed)
		break
while True:
	if can_harvest():
		harvest()
		if num_items(Items.Hay) == 30:
			unlock(Unlocks.Expand)
			break
while True:
	harvest()
	move(North)
	if num_items(Items.Hay) == 50:
		unlock(Unlocks.Plant)
		break

EarlyHayandBush(10)
unlock(Unlocks.Grass)
EarlyHayandBush(11)
unlock(Unlocks.Expand)
PlantAll(Entities.Bush)
FarmAll(Entities.Bush)
Home()
HarvestAll()
unlock(Unlocks.Speed)
Home()
PlantRow(East, Entities.Bush, Items.Carrot_Seed)
move(North)
PlantRow(West, Entities.Bush, Items.Cactus_Seed)
move(North)
PlantRow(East, Entities.Grass, Items.Carrot_Seed)
move(North)
move(East)
exit = False
while True:
	FarmRow(East, Entities.Bush, Items.Carrot_Seed)
	move(North)
	FarmRow(West, Entities.Bush, Items.Carrot_Seed)
	move(North)
	FarmRow(East, Entities.Grass, Items.Carrot_Seed)
	move(North)
	move(East)
	unlock(Unlocks.Grass)
	if unlock(Unlocks.Carrots):
		exit = True
	if exit and num_items(Items.Wood) > 250 and num_items(Items.Hay) > 100: 
		break
PlantAll(Entities.Carrots, Items.Carrot_Seed)
while True:
	FarmAll(Entities.Carrots, Items.Carrot_Seed)
	if unlock(Unlocks.Expand):
		break
PlantAll(Entities.Carrots, Items.Carrot_Seed)
while True:
	FarmAll(Entities.Carrots, Items.Carrot_Seed)
	if unlock(Unlocks.Trees):
		break
PlantAllTree()
while num_items(Items.Wood) < 100:
	FarmAllTree()
PlantAll(Entities.Carrots, Items.Carrot_Seed)
while True:
	FarmAll(Entities.Carrots, Items.Carrot_Seed)
	if unlock(Unlocks.Speed):
		break
PlantAll(Entities.Grass, Items.Carrot_Seed)
while True:
	FarmAll(Entities.Grass, Items.Carrot_Seed)
	if unlock(Unlocks.Trees):
		break
PlantAll(Entities.Grass, Items.Carrot_Seed)
while True:
	FarmAll(Entities.Grass, Items.Carrot_Seed)
	if unlock(Unlocks.Grass):
		break
PlantAll(Entities.Grass, Items.Carrot_Seed)
for i in range(15):
	FarmAll(Entities.Grass, Items.Carrot_Seed)
	unlock(Unlocks.Trees)
PlantAll(Entities.Grass, Items.Carrot_Seed)
for i in range(10):
	FarmAll(Entities.Grass, Items.Carrot_Seed)
PlantAllTree()
while num_items(Items.Wood) < 1500:
	FarmAllTree()
PlantAll(Entities.Carrots, Items.Carrot_Seed)
while True:
	FarmAll(Entities.Carrots, Items.Carrot_Seed)
	unlock(Unlocks.Speed)
	if unlock(Unlocks.Sunflowers):
		break
PlantAll(Entities.Carrots, Items.Carrot_Seed)
for i in range(5):
	FarmAll(Entities.Carrots, Items.Carrot_Seed)
main()