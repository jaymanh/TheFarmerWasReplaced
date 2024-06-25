def Maze():
	# Define the directions and their vectors
	HarvestAll()
	Home()
	DIRECTIONS = [North, South, West, East]
	DIRECTION_VECTORS = {North: (0, -1), South: (0, 1), West: (-1, 0), East: (1, 0)}
	REVERSE_DIRECTION = {North: South, South: North, West: East, East: West}
	
	visited = set()
	j = 0
	def solve_maze():
		def dfs(x, y):
	        # Mark the current cell as visited
			visited.add((x, y))
	        # Check if the current position has the treasure	        
			if get_entity_type() == Entities.Treasure and j > 298:
				harvest()
				plant(Entities.Bush)
				while(get_entity_type() == Entities.Bush):
					if(num_items(Items.Fertilizer) < 10):
						if not trade(Items.Fertilizer, 10):
							j = 298
							return True
					use_item(Items.Fertilizer)
				return True
			elif get_entity_type() == Entities.Treasure:
				while(get_entity_type() == Entities.Treasure):
					if(num_items(Items.Fertilizer) < 10):
						if not trade(Items.Fertilizer, 10):
							j = 298
							return
					use_item(Items.Fertilizer)
				return True
	
	        # Try moving in all four directions
			for i in range(4):
				direction = DIRECTIONS[i]
				dx, dy = DIRECTION_VECTORS[direction]
				new_x, new_y = x + dx, y + dy
			
				if (new_x, new_y) not in visited:
					if move(direction):
						if dfs(new_x, new_y):
							return True
						# Backtrack if moving in the current direction didn't lead to the treasure
						move(REVERSE_DIRECTION[direction])
	
			return False
	
	    # Start DFS from the initial position (0, 0)
		initial_x, initial_y = get_pos_x(), get_pos_y()
		dfs(initial_x, initial_y)
	
	plant(Entities.Bush)
	while(get_entity_type() == Entities.Bush):
		if(num_items(Items.Fertilizer) < 10):
			if not trade(Items.Fertilizer, 10):
				return
		use_item(Items.Fertilizer)
	while(j < 300):
		visited = set()
		solve_maze()
		j += 1
	harvest()
a = get_time()
Maze()
quick_print(get_time() - a)