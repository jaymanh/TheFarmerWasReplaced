def EarlyHayandBush(j = 10):
	Home()
	for i in range(j):
		move(South)
		harvest()
		plant(Entities.Bush)
		move(North)
		for k in range(5):
			harvest()
			move(North)
			harvest()
			move(South)
		harvest()
	
set_farm_size(3)
set_execution_speed(1)
EarlyHayandBush()