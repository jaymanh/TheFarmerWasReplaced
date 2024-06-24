world = get_world_size()
harvest()
Home()
harvest()

# Define the directions and their vectors
DIRECTIONS = [North, South, West, East]
DIRECTION_VECTORS = {North: (0, -1), South: (0, 1), West: (-1, 0), East: (1, 0)}
REVERSE_DIRECTION = {North: South, South: North, West: East, East: West}

visited = set()

def solve_maze():
    def dfs(x, y):
        # Mark the current cell as visited
        visited.add((x, y))
        # Check if the current position has the treasure
        if get_entity_type() == Entities.Treasure:
			harvest()
			plant(Entities.Bush)
			while(get_entity_type() == Entities.Bush):
				if(num_items(Items.Fertilizer) < 10):
					trade(Items.Fertilizer, 10)
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
		trade(Items.Fertilizer, 10)
	use_item(Items.Fertilizer)
		
while(True):
	solve_maze()
	visited = set()
		
	
